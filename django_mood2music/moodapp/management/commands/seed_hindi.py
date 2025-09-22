from django.core.management.base import BaseCommand
from moodapp.models import Song


HINDI_SONGS = [
    {"title": "Kabira", "artist": "Arijit Singh", "mood": "Happy", "link": "https://www.youtube.com/watch?v=jHNNMj5bNQw"},
    {"title": "Ilahi", "artist": "Arijit Singh", "mood": "Excited", "link": "https://www.youtube.com/watch?v=DCQNmMRMItA"},
    {"title": "Agar Tum Saath Ho", "artist": "Alka Yagnik", "mood": "Sad", "link": "https://www.youtube.com/watch?v=sK7riqg2mr4"},
    {"title": "Kun Faya Kun", "artist": "Javed Ali", "mood": "Relaxed", "link": "https://www.youtube.com/watch?v=T94PHkuydcw"},
    {"title": "Zinda", "artist": "Siddharth Mahadevan", "mood": "Stressed", "link": "https://www.youtube.com/watch?v=cNw8A5pwbVI"},
    {"title": "Bhaag DK Bose", "artist": "Ram Sampath", "mood": "Angry", "link": "https://www.youtube.com/watch?v=Q2GS1Ul8T_0"},
    {"title": "Tera Yaar Hoon Main", "artist": "Arijit Singh", "mood": "Relaxed", "link": "https://www.youtube.com/watch?v=dx4Teh-nv3A"},
    {"title": "Channa Mereya", "artist": "Arijit Singh", "mood": "Sad", "link": "https://www.youtube.com/watch?v=284Ov7ysmfA"},
]


class Command(BaseCommand):
    help = "Seed Hindi songs for various moods"

    def handle(self, *args, **options):
        created = 0
        for s in HINDI_SONGS:
            obj, was_created = Song.objects.get_or_create(
                title=s["title"], artist=s["artist"], defaults={"mood": s["mood"], "link": s["link"]}
            )
            if was_created:
                created += 1
        self.stdout.write(self.style.SUCCESS(f"Seeded {created} Hindi songs."))


