from collections import Counter
import requests
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from .models import Song, History


def home(request):
    return render(request, "home.html")


def register_view(request):
    if request.user.is_authenticated:
        return redirect("dashboard")
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful. Please log in.")
            return redirect("login")
    else:
        form = UserCreationForm()
    return render(request, "register.html", {"form": form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect("dashboard")
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "Logged in successfully.")
            return redirect("dashboard")
    else:
        form = AuthenticationForm()
    return render(request, "login.html", {"form": form})


def logout_view(request):
    logout(request)
    messages.info(request, "You have been logged out.")
    return redirect("login")


@login_required
def dashboard(request):
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

    return render(request, "dashboard.html", {"moods": moods, "quote_text": quote_text, "quote_author": quote_author})


@login_required
def playlist(request, mood: str):
    normalized = mood.capitalize()
    songs = Song.objects.filter(mood__iexact=normalized)
    History.objects.create(user=request.user, mood=normalized)
    return render(request, "playlist.html", {"mood": normalized, "songs": songs})


@login_required
def add_song(request):
    if request.method == "POST":
        title = request.POST.get("title", "").strip()
        artist = request.POST.get("artist", "").strip()
        mood = request.POST.get("mood", "").strip()
        link = request.POST.get("link", "").strip()
        if not title or not artist or not mood or not link:
            messages.warning(request, "All fields are required.")
        else:
            Song.objects.create(title=title, artist=artist, mood=mood.capitalize(), link=link)
            messages.success(request, "Song added successfully!")
            return redirect("playlist", mood=mood)
    return render(request, "add_song.html")


@login_required
def history(request):
    records = request.user.histories.all()
    mood_counts = Counter(r.mood for r in records)
    labels = list(mood_counts.keys())
    counts = [mood_counts[l] for l in labels]
    return render(request, "history.html", {"records": records, "labels": labels, "counts": counts})


