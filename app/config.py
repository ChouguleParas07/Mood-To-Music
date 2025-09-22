import os


class Config:
    """Configuration for Mood2Music app."""

    def __init__(self) -> None:
        # Secret key for session signing
        self.SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret-change-me")

        # Optional MySQL configuration via environment
        mysql_user = os.getenv("MYSQL_USER")
        mysql_password = os.getenv("MYSQL_PASSWORD")
        mysql_host = os.getenv("MYSQL_HOST", "127.0.0.1")
        mysql_db = os.getenv("MYSQL_DATABASE")

        if mysql_user and mysql_password and mysql_db:
            # Use MySQL if credentials are provided
            self.SQLALCHEMY_DATABASE_URI = (
                f"mysql+pymysql://{mysql_user}:{mysql_password}@{mysql_host}/{mysql_db}?charset=utf8mb4"
            )
        else:
            # Fallback to SQLite for local development
            basedir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
            self.SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "mood2music.db")

        self.SQLALCHEMY_TRACK_MODIFICATIONS = False


