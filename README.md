# Mood2Music – Emotion-Based Playlist Generator

A Flask web app that recommends playlists based on your mood, with user auth, song management, and mood history charts.

## Features
- User registration, login, logout (Flask-Login)
- Dashboard mood selection with emoji buttons and optional Quote of the Day
- Playlist by mood from database; add your own songs
- History tracking and Chart.js analytics
- Bootstrap 5 responsive UI

## Tech Stack
- Python, Flask, Flask-Login, Flask-SQLAlchemy
- MySQL (via PyMySQL) or SQLite fallback
- Bootstrap 5, Chart.js

## Getting Started

### 1) Create and activate a virtual environment (Windows PowerShell)
```bash
python -m venv .venv
. .venv/Scripts/Activate.ps1
```

### 2) Install dependencies
```bash
pip install -r requirements.txt
```

### 3) Configure environment
Create a file named `.env` in the project root. To use MySQL, set:
```
MYSQL_USER=your_user
MYSQL_PASSWORD=your_password
MYSQL_HOST=127.0.0.1
MYSQL_DATABASE=mood2music
SECRET_KEY=change-me
```
If MySQL vars are not set, the app will use a local SQLite file `mood2music.db` in the repo root.

### 4) Run the app
```bash
python run.py
```
App will start at `http://127.0.0.1:5000`.

### 5) Seed example songs (optional)
```bash
python scripts/seed_songs.py
```

## Database Schema
- users(id INT PK, username VARCHAR, email VARCHAR, password VARCHAR)
- songs(id INT PK, title VARCHAR, artist VARCHAR, mood VARCHAR, link VARCHAR)
- history(id INT PK, user_id INT FK, mood VARCHAR, datetime TIMESTAMP)

## Notes
- Protected routes: `dashboard`, `playlist/<mood>`, `add_song`, `history`
- Quote API: `https://api.quotable.io/random` (best-effort; failures are ignored)

## License
MIT
