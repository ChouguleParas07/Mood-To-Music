from django.contrib import admin
from .models import Song, History


@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ("title", "artist", "mood")
    search_fields = ("title", "artist", "mood")
    list_filter = ("mood",)


@admin.register(History)
class HistoryAdmin(admin.ModelAdmin):
    list_display = ("user", "mood", "created_at")
    list_filter = ("mood", "created_at")


