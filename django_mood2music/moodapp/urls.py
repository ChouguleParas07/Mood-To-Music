from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("playlist/<str:mood>/", views.playlist, name="playlist"),
    path("add-song/", views.add_song, name="add_song"),
    path("history/", views.history, name="history"),

    path("register/", views.register_view, name="register"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
]


