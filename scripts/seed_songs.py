import os
import sys

# Ensure project root is on sys.path when running from scripts/
CURRENT_DIR = os.path.dirname(__file__)
PROJECT_ROOT = os.path.abspath(os.path.join(CURRENT_DIR, ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from app import create_app, db
from app.models import Song


SEED_SONGS = [
    {"title": "Happy - Pharrell Williams", "artist": "Pharrell Williams", "mood": "Happy", "link": "https://www.youtube.com/watch?v=ZbZSe6N_BXs"},
    {"title": "Don't Worry Be Happy", "artist": "Bobby McFerrin", "mood": "Happy", "link": "https://www.youtube.com/watch?v=d-diB65scQU"},
    {"title": "Someone Like You", "artist": "Adele", "mood": "Sad", "link": "https://www.youtube.com/watch?v=hLQl3WQQoQ0"},
    {"title": "Fix You", "artist": "Coldplay", "mood": "Sad", "link": "https://www.youtube.com/watch?v=k4V3Mo61fJM"},
    {"title": "Eye of the Tiger", "artist": "Survivor", "mood": "Excited", "link": "https://www.youtube.com/watch?v=btPJPFnesV4"},
    {"title": "Can't Hold Us", "artist": "Macklemore & Ryan Lewis", "mood": "Excited", "link": "https://www.youtube.com/watch?v=2zNSgSzhBfM"},
    {"title": "Weightless", "artist": "Marconi Union", "mood": "Relaxed", "link": "https://www.youtube.com/watch?v=UfcAVejslrU"},
    {"title": "Clair de Lune", "artist": "Claude Debussy", "mood": "Relaxed", "link": "https://www.youtube.com/watch?v=CvFH_6DNRCY"},
    {"title": "Break Stuff", "artist": "Limp Bizkit", "mood": "Angry", "link": "https://www.youtube.com/watch?v=ZpUYjpKg9KY"},
    {"title": "Killing In The Name", "artist": "Rage Against The Machine", "mood": "Angry", "link": "https://www.youtube.com/watch?v=bWXazVhlyxQ"},
    {"title": "Weight of the World", "artist": "Earth", "mood": "Stressed", "link": "https://open.spotify.com/track/6rC71gYpU0wgjXfVC9+"},
]


def main():
    app = create_app()
    with app.app_context():
        for s in SEED_SONGS:
            exists = Song.query.filter_by(title=s["title"], artist=s["artist"], mood=s["mood"].capitalize()).first()
            if exists:
                continue
            song = Song(title=s["title"], artist=s["artist"], mood=s["mood"].capitalize(), link=s["link"])
            db.session.add(song)
        db.session.commit()
        print("Seeded songs.")


if __name__ == "__main__":
    main()


