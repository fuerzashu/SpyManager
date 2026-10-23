"""Command-line interface for SpyManager."""
import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

from rich.console import Console
from rich.panel import Panel
from rich.progress import BarColumn, Progress, SpinnerColumn, TextColumn, TimeElapsedColumn
from rich.table import Table
from rich.text import Text

from . import __version__
from .i18n import get_text
from .scanner import scan_username
from .sites import SITES

console = Console()
USERNAME_RE = re.compile(r"^[A-Za-z0-9_.-]{1,39}$")
BANNER = r"""
  ____              __  __
 / ___| _ __  _   _|  \/  | __ _ _ __   __ _  __ _  ___ _ __
 \___ \| '_ \| | | | |\/| |/ _` | '_ \ / _` |/ _` |/ _ \ '__|
  ___) | |_) | |_| | |  | | (_| | | | | (_| | (_| |  __/ |
 |____/| .__/ \__, |_|  |_|\__,_|_| |_|\__,_|\__, |\___|_|
       |_|    |___/                          |___/
"""

def build_parser():
    parser = argparse.ArgumentParser(
        prog="spymanager",
        description="Check public profile URL patterns for a username.",
    )
    parser.add_argument("username", nargs="?", help="username to check")
    parser.add_argument("--lang", choices=["en", "ru"], default="en", help="interface language: en or ru")
    parser.add_argument("--timeout", type=float, default=8.0, help="request timeout in seconds (0.5–60)")
    parser.add_argument("--workers", type=int, default=4, help="parallel requests (1–8)")
    parser.add_argument("--json", dest="json_path", metavar="FILE", help="export results as JSON")
    parser.add_argument("--txt", dest="txt_path", metavar="FILE", help="export results as TXT")
    parser.add_argument("--sites", action="store_true", help="list supported sites")
    parser.add_argument("--version", action="version", version=f"%(prog)s {__version__}")
    return parser

def main(argv=None):
    args = build_parser().parse_args(argv)
    t = lambda key: get_text(args.lang, key)

    if args.sites:
        table = Table(title=t("sites_title"), border_style="cyan")
        table.add_column(t("site"))
        table.add_column(t("category"))
        table.add_column(t("url"), overflow="fold")
        for site in SITES:
            table.add_row(site.name, site.category, site.template)
        console.print(table)
        return 0
    if not args.username:
        console.print("[yellow]Provide a username, e.g. python spymanager.py octocat --lang ru[/yellow]")
        return 2
    if not USERNAME_RE.fullmatch(args.username):
        console.print(f"[bold red]{t('invalid')}[/bold red]")
        return 2
    if not 0.5 <= args.timeout <= 60:
        console.print(f"[red]{t('timeout_error')}[/red]")
        return 2
    if not 1 <= args.workers <= 8:
        console.print(f"[red]{t('workers_error')}[/red]")
        return 2

    console.print(Text(BANNER, style="bold cyan"))
    console.print(Panel.fit(
        f"[bold]{t('title')}[/bold] [dim]v{__version__}[/dim]\n"
        f"{t('subtitle')}\n[white]{t('target')}:[/white] [bold yellow]{args.username}[/bold yellow]",
        border_style="cyan",
    ))
    console.print(f"[dim]{t('warning')}[/dim]\n")

    try:
        with Progress(
            SpinnerColumn(),
            TextColumn("{task.description}"),
            BarColumn(),
            TextColumn("{task.completed}/{task.total}"),
            TimeElapsedColumn(),
            console=console,
        ) as progress:
            task = progress.add_task("Scanning public profile URLs...", total=len(SITES))
            results = scan_username(
                args.username, timeout=args.timeout, workers=args.workers,
                language=args.lang, progress=lambda done, total: progress.update(task, completed=done)
            )
    except KeyboardInterrupt:
        console.print(f"\n[yellow]{t('interrupted')}[/yellow]")
        return 130

    table = Table(title=t("results"), border_style="cyan", header_style="bold")
    table.add_column(t("site"), no_wrap=True)
    table.add_column(t("category"))
    table.add_column(t("status"), no_wrap=True)
    table.add_column(t("url"), overflow="fold")
    table.add_column(t("details"), overflow="fold")
    labels = {
        "CHECK": ("yellow", t("check_status")),
        "NOT FOUND": ("red", t("not_found_status")),
        "UNKNOWN": ("magenta", t("unknown_status")),
        "ERROR": ("red", t("error_status")),
    }
    for r in results:
        color, label = labels[r.status]
        table.add_row(r.site, r.category, f"[{color}]{label}[/{color}]", r.url, r.detail)
    console.print(table)

    checked = sum(r.status == "CHECK" for r in results)
    missing = sum(r.status == "NOT FOUND" for r in results)
    uncertain = sum(r.status in ("UNKNOWN", "ERROR") for r in results)
    console.print(
        f"\n[bold]{t('summary')}:[/bold] [yellow]{checked} {t('check')}[/yellow] · "
        f"[red]{missing} {t('not_found')}[/red] · [magenta]{uncertain} {t('uncertain')}[/magenta]"
    )
    console.print(f"[dim]{t('note')}[/dim]")

    payload = {
        "tool": "SpyManager",
        "version": __version__,
        "language": args.lang,
        "username": args.username,
        "scanned_at_utc": datetime.now(timezone.utc).isoformat(),
        "note": "HTTP 200 results require manual verification; results are indicative only.",
        "results": [
            {"site": r.site, "category": r.category, "url": r.url,
             "status": r.status, "detail": r.detail}
            for r in results
        ],
    }
    for path, kind in ((args.json_path, "json"), (args.txt_path, "txt")):
        if not path:
            continue
        try:
            if kind == "json":
                content = json.dumps(payload, indent=2, ensure_ascii=False) + "\n"
            else:
                content = "\n".join(
                    [f"SpyManager results for {args.username}", f"Scanned at: {payload['scanned_at_utc']}", ""] +
                    [f"{r.site}: {r.status} — {r.url} — {r.detail}" for r in results]
                ) + "\n"
            Path(path).write_text(content, encoding="utf-8")
            console.print(f"[green]{t('saved_json' if kind == 'json' else 'saved_txt')}:[/green] {path}")
        except OSError as exc:
            console.print(f"[red]{t('write_error')}:[/red] {exc}")
            return 1
    return 0
