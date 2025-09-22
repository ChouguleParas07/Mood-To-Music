from collections import Counter
from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from . import db
from .models import Song, History
import requests


main_bp = Blueprint("main", __name__)


@main_bp.route("/")
def home():
    return render_template("home.html")


@main_bp.route("/dashboard")
@login_required
def dashboard():
    moods = [
        {"name": "Happy", "color": "#f59e0b", "emoji": "😄"},
        {"name": "Sad", "color": "#3b82f6", "emoji": "😢"},
        {"name": "Stressed", "color": "#ef4444", "emoji": "😖"},
        {"name": "Excited", "color": "#22c55e", "emoji": "🤩"},
        {"name": "Relaxed", "color": "#0ea5e9", "emoji": "😌"},
        {"name": "Angry", "color": "#b91c1c", "emoji": "😡"},
    ]

    quote_text = None
    quote_author = None
    try:
        resp = requests.get("https://api.quotable.io/random", timeout=5)
        if resp.ok:
            data = resp.json()
            quote_text = data.get("content")
            quote_author = data.get("author")
    except Exception:
        pass

    return render_template("dashboard.html", moods=moods, quote_text=quote_text, quote_author=quote_author)


@main_bp.route("/playlist/<mood>")
@login_required
def playlist(mood: str):
    normalized = mood.capitalize()
    songs = Song.query.filter(Song.mood.ilike(normalized)).all()

    # Record mood selection history
    try:
        entry = History(user_id=current_user.id, mood=normalized)
        db.session.add(entry)
        db.session.commit()
    except Exception:
        db.session.rollback()

    return render_template("playlist.html", mood=normalized, songs=songs)


@main_bp.route("/add_song", methods=["GET", "POST"])
@login_required
def add_song():
    if request.method == "POST":
        title = request.form.get("title", "").strip()
        artist = request.form.get("artist", "").strip()
        mood = request.form.get("mood", "").strip()
        link = request.form.get("link", "").strip()

        if not title or not artist or not mood or not link:
            flash("All fields are required.", "warning")
            return render_template("add_song.html")

        song = Song(title=title, artist=artist, mood=mood.capitalize(), link=link)
        db.session.add(song)
        db.session.commit()
        flash("Song added successfully!", "success")
        return redirect(url_for("main.playlist", mood=mood))

    return render_template("add_song.html")


@main_bp.route("/history")
@login_required
def history():
    records = History.query.filter_by(user_id=current_user.id).order_by(History.datetime.desc()).all()
    mood_counts = Counter([r.mood for r in records])
    labels = list(mood_counts.keys())
    counts = [mood_counts[label] for label in labels]

    return render_template("history.html", records=records, labels=labels, counts=counts)


