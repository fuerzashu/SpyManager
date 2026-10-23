"""Concurrent, conservative checks for public profile URLs."""
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass
from urllib.parse import quote

import requests

from .i18n import get_text
from .sites import Site, SITES

@dataclass
class ScanResult:
    site: str
    category: str
    url: str
    status: str
    detail: str

def _check(site: Site, username: str, timeout: float, language: str) -> ScanResult:
    url = site.template.format(username=quote(username, safe=""))
    headers = {"User-Agent": "SpyManager/2.0 (public profile URL checker)"}
    t = lambda key: get_text(language, key)
    try:
        response = requests.get(url, headers=headers, timeout=timeout, allow_redirects=True)
    except requests.Timeout:
        return ScanResult(site.name, site.category, url, "ERROR", t("timeout"))
    except requests.RequestException:
        return ScanResult(site.name, site.category, url, "ERROR", t("request_failed"))

    code = response.status_code
    if code == 404:
        return ScanResult(site.name, site.category, url, "NOT FOUND", t("http404"))
    if code == 429:
        return ScanResult(site.name, site.category, url, "UNKNOWN", t("rate_limited"))
    if code in (401, 403):
        return ScanResult(site.name, site.category, url, "UNKNOWN", f'{t("restricted")} (HTTP {code})')
    if 300 <= code < 400:
        return ScanResult(site.name, site.category, url, "UNKNOWN", t("redirect"))
    if code >= 500:
        return ScanResult(site.name, site.category, url, "UNKNOWN", f'{t("site_error")} (HTTP {code})')
    if code == 200:
        # Generic pages and soft-404s are common, so don't claim a profile was found.
        return ScanResult(site.name, site.category, url, "CHECK", t("http200"))
    return ScanResult(site.name, site.category, url, "UNKNOWN", f'{t("unknown_http")} (HTTP {code})')

def scan_username(username: str, timeout: float = 8.0, workers: int = 4,
                  sites=SITES, language: str = "en", progress=None) -> list[ScanResult]:
    sites = list(sites)
    results = []
    with ThreadPoolExecutor(max_workers=max(1, min(workers, 8))) as pool:
        futures = {pool.submit(_check, site, username, timeout, language): site for site in sites}
        completed = 0
        for future in as_completed(futures):
            results.append(future.result())
            completed += 1
            if progress:
                progress(completed, len(sites))
    order = {site.name: i for i, site in enumerate(sites)}
    return sorted(results, key=lambda r: order[r.site])
