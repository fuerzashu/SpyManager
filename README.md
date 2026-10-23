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


---

# SpyManager 🔎 — Русская версия

**Быстрый мультиязычный инструмент для проверки публичных ссылок на профили пользователей.**

SpyManager проверяет, могут ли существовать публичные страницы профилей, связанные с указанным именем пользователя, на различных платформах. Программа поддерживает работу в терминале, параллельные проверки и экспорт результатов в JSON/TXT.

> **Отказ от ответственности:** SpyManager — это OSINT-инструмент для проверки общедоступных ссылок на профили. Он не получает доступ к приватным аккаунтам, не обходит аутентификацию и не гарантирует, что имя пользователя принадлежит конкретному человеку.

## ✨ Возможности

- 🌐 Проверка имён пользователей на 20 платформах
- 🚀 Параллельное выполнение проверок для ускорения работы
- 🌍 Английский и русский интерфейс
- 🎨 Цветной вывод в терминале с индикатором прогресса
- 📄 Экспорт результатов в JSON или TXT
- ⚙️ Возможность выбирать конкретные платформы для проверки
- ⏱️ Настройка тайм-аутов запросов и количества рабочих потоков
- 🐍 Совместимость с Python 3.10 и новее

## 🌍 Поддерживаемые платформы

GitHub · GitLab · Codeberg · Bitbucket · Hugging Face · PyPI · Reddit · Medium · DEV Community · Hashnode · Twitch · YouTube · GitBook · Keybase · Mastodon.social · Docker Hub · Replit · Kaggle · Instructables · Scratch

## 📦 Установка

**Требования:** Python 3.10 или новее; Git — необязательно.

### 1. Клонирование репозитория

```bash
git clone https://github.com/fuerzashu/SpyManager.git
cd SpyManager
```

Также можно скачать репозиторий в формате ZIP и распаковать архив.

### 2. Установка зависимостей

```bash
python -m pip install -r requirements.txt
```

В некоторых системах вместо `python` необходимо использовать `python3`.

## 🚀 Использование

### Проверка имени пользователя

```bash
python spymanager.py example --lang en
```

### Запуск русского интерфейса

```bash
python spymanager.py example --lang ru
```

### Список поддерживаемых платформ

```bash
python spymanager.py --sites
```

### Экспорт результатов

```bash
python spymanager.py example --json results.json --txt results.txt
```

### Просмотр всех доступных параметров

```bash
python spymanager.py --help
```

## 📊 Как понимать результаты

SpyManager сообщает результат проверки каждой публичной ссылки на профиль.

- **Found / Possible match (Найдено / Возможное совпадение):** страница может существовать и требует ручной проверки.
- **Not found (Не найдено):** платформа вернула ответ, который был интерпретирован как отсутствие доступного профиля.
- **Unknown / Error (Неизвестно / Ошибка):** результат не удалось достоверно определить.

**Важно:** HTTP-коды состояния и ответы платформ не являются окончательным доказательством существования или отсутствия аккаунта. На результаты могут влиять перенаправления, ограничения частоты запросов, ограничения доступа и изменения сайтов.

## 🛠️ Структура проекта

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

## 🌐 Языки

- English: `README.md`
- Русский: [README_RU.md](README_RU.md)

## 🔒 Ответственное использование

Используйте SpyManager ответственно и соблюдайте условия использования каждой платформы, ограничения частоты запросов и правила конфиденциальности. Используйте результаты только в законных целях.

## 🤝 Участие в разработке

Предложения, сообщения об ошибках и pull request приветствуются!

1. Создайте форк репозитория.
2. Создайте отдельную ветку для изменений.
3. Внесите необходимые изменения.
4. Отправьте pull request.

## 📄 Лицензия

Проект распространяется по лицензии MIT. Подробности находятся в файле [LICENSE](LICENSE).

---

**Если SpyManager оказался полезен, поставьте проекту ⭐ на GitHub!**
