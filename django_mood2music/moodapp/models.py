from django.db import models
from django.contrib.auth.models import User


class Song(models.Model):
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    mood = models.CharField(max_length=50, db_index=True)
    link = models.URLField(max_length=500)

    def __str__(self) -> str:
        return f"{self.title} - {self.artist} ({self.mood})"


class History(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="histories")
    mood = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]


