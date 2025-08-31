import os
from dotenv import load_dotenv

load_dotenv()  # Load .env file

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "default_secret_key")
    DEBUG = os.getenv("FLASK_ENV") == "development"