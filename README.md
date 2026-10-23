# SpyManager 🔎

**A fast, multilingual username checker for public profile URLs.**

SpyManager checks whether public profile pages associated with a username may exist across multiple platforms. It features a terminal interface, parallel checks, and JSON/TXT exports.

> **Disclaimer:** SpyManager is an OSINT utility for checking publicly accessible profile URLs. It does not access private accounts, bypass authentication, or guarantee that a username belongs to a particular person.

## ✨ Features

- 🌐 Check usernames across 20 platforms
- 🚀 Run checks concurrently for faster results
- 🌍 English and Russian interface
- 🎨 Colorful terminal output with a progress bar
- 📄 Export results to JSON or TXT
- ⚙️ Choose specific platforms to check
- ⏱️ Configure request timeouts and worker count
- 🐍 Works with Python 3.10+

## 🌍 Supported Platforms

GitHub · GitLab · Codeberg · Bitbucket · Hugging Face · PyPI · Reddit · Medium · DEV Community · Hashnode · Twitch · YouTube · GitBook · Keybase · Mastodon.social · Docker Hub · Replit · Kaggle · Instructables · Scratch

## 📦 Installation

**Requirements:** Python 3.10 or newer and Git (optional).

### 1. Clone the repository

```bash
git clone https://github.com/fuerzashu/SpyManager.git
cd SpyManager
```

Alternatively, download the repository as a ZIP file and extract it.

### 2. Install dependencies

```bash
python -m pip install -r requirements.txt
```

On some systems, use `python3` instead of `python`.

## 🚀 Usage

### Check a username

```bash
python spymanager.py example --lang en
```

### Use the Russian interface

```bash
python spymanager.py example --lang ru
```

### List supported platforms

```bash
python spymanager.py --sites
```

### Export results

```bash
python spymanager.py example --json results.json --txt results.txt
```

### View all available options

```bash
python spymanager.py --help
```

## 📊 Understanding Results

SpyManager reports the outcome of checking each public profile URL.

- **Found / Possible match:** The page may exist and needs manual verification.
- **Not found:** The platform returned a response interpreted as an unavailable profile.
- **Unknown / Error:** The result could not be reliably determined.

**Important:** HTTP status codes and platform responses are not definitive proof that an account exists or does not exist. Results can be affected by redirects, rate limits, access restrictions, and changes to platform websites.

## 🛠️ Project Structure

```text
SpyManager/
├── spymanager.py
├── spymanager/
│   ├── __init__.py
│   ├── cli.py
│   ├── i18n.py
│   ├── scanner.py
│   └── sites.py
├── requirements.txt
├── pyproject.toml
├── LICENSE
├── README.md
└── README_RU.md
```

## 🌐 Languages

- English: `README.md`
- Русский: [README_RU.md](README_RU.md)

## 🔒 Responsible Use

Use SpyManager responsibly and respect each platform's terms of service, rate limits, and privacy rules. Only use the results for legitimate purposes.

## 🤝 Contributing

Suggestions, bug reports, and pull requests are welcome!

1. Fork the repository.
2. Create a feature branch.
3. Make your changes.
4. Submit a pull request.

## 📄 License

This project is distributed under the MIT License. See [LICENSE](LICENSE).

---

**If you find SpyManager useful, consider giving the project a ⭐ on GitHub!**
