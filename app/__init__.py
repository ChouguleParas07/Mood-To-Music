import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from dotenv import load_dotenv

# Initialize extensions without app; bind in create_app
db = SQLAlchemy()
login_manager = LoginManager()


def create_app() -> Flask:
    """Application factory for Mood2Music."""
    # Load environment variables from a .env file if present
    load_dotenv()

    app = Flask(__name__, static_folder="static", template_folder="templates")

    # Configuration
    from .config import Config
    app.config.from_object(Config())

    # Initialize extensions
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = "auth.login"

    # Import models to ensure tables are registered
    from . import models  # noqa: F401

    # Register blueprints
    from .auth import auth_bp
    from .routes import main_bp
    app.register_blueprint(auth_bp)
    app.register_blueprint(main_bp)

    # Create database tables on first run
    with app.app_context():
        db.create_all()

    return app


__all__ = ["create_app", "db", "login_manager"]


