# Mood2Music – Emotion-Based Playlist Generator

Mood-based playlist app with authentication, song management, mood history charts, and a modern UI. This repository includes both Flask and Django implementations—use whichever you prefer.

## AUTHER -> "Paras Chougule"

## Features
- User authentication (register, login, logout)
- Dashboard with emoji mood selection + optional Quote of the Day
- Playlist recommendations by mood; add your own songs with links (YouTube/Spotify)
- Mood history tracking and Chart.js visualizations
- Attractive UI (Bootstrap 5, Google Fonts, Boxicons, gradients, glassmorphism)

## Prerequisites
- Python 3.13 installed
- Windows PowerShell (commands below use PS syntax)

## Quick Start

1) Create and activate a virtual environment
```bash
python -m venv .venv
. .venv/Scripts/Activate.ps1
```

2) Install all dependencies
```bash
pip install -r requirements.txt
```

3) Choose a stack to run (Flask or Django) and follow the relevant section below.

---

## Flask App

Flask app lives at the project root.

1) Environment (MySQL optional; SQLite is default)
Create `.env` in the project root if you want MySQL:
```
SECRET_KEY=change-me
MYSQL_USER=your_user
MYSQL_PASSWORD=your_password
MYSQL_HOST=127.0.0.1
MYSQL_DATABASE=mood2music
```
If not set, the app uses a local SQLite file `mood2music.db`.

2) Run Flask
```bash
python run.py
```
Open `http://127.0.0.1:5000`.

3) Seed example songs (optional)
```bash
python scripts/seed_songs.py
```

Flask routes: `/register`, `/login`, `/dashboard`, `/playlist/<mood>`, `/add_song`, `/history`, `/logout`

---

## Django App

Django project path: `django_mood2music/`

1) Apply migrations
```bash
python django_mood2music/manage.py makemigrations
python django_mood2music/manage.py migrate
```

2) Seed Hindi songs (optional)
```bash
python django_mood2music/manage.py seed_hindi
```

3) Run Django
```bash
python django_mood2music/manage.py runserver 127.0.0.1:8000
```
Open `http://127.0.0.1:8000`.

Django routes: `/register`, `/login`, `/dashboard`, `/playlist/<mood>/`, `/add-song/`, `/history`, `/logout`

Admin (optional):
```bash
python django_mood2music/manage.py createsuperuser
```

---

## UI / Assets
- Flask styles: `app/static/css/styles.css`
- Django styles: `django_mood2music/static/css/styles.css`
- Icons: Boxicons CDN
- Fonts: Google Fonts (Poppins)
- Favicon: `django_mood2music/static/favicon.svg`

## Troubleshooting
- If `pip` inside the venv is missing: `python -m ensurepip --upgrade`
- Port already in use: change port (`runserver 127.0.0.1:8001` or `app.run(port=5001)`)
- Verify you’re using venv Python: `.\.venv\Scripts\python.exe --version`

## License
MIT
