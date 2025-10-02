"""
Application configuration
"""
import os
from dotenv import load_dotenv

load_dotenv()

class Config:  # pylint: disable=too-few-public-methods
    """Base configuration"""
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key-change-in-production'
    FLASK_ENV = os.environ.get('FLASK_ENV') or 'development'
    FLASK_DEBUG = os.environ.get('FLASK_DEBUG', 'True').lower() == 'true'
    HOST = os.environ.get('HOST') or '127.0.0.1'
    PORT = int(os.environ.get('PORT') or 5000)

    # Window configuration
    WINDOW_TITLE = os.environ.get('WINDOW_TITLE') or 'PyWebView + Svelte Application'
    WINDOW_WIDTH = int(os.environ.get('WINDOW_WIDTH') or 1200)
    WINDOW_HEIGHT = int(os.environ.get('WINDOW_HEIGHT') or 800)
    WINDOW_MIN_SIZE = (800, 600)
