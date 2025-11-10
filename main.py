"""Flask application for CI/CD demonstration."""
import os
from flask import Flask
from dotenv import load_dotenv

# Загружаем переменные окружения из .env
load_dotenv()

app = Flask(__name__)

# Получаем версию приложения из .env, если нет — используем значение по умолчанию
APP_VERSION = os.getenv("APP_VERSION", "0.0.0")


@app.route("/")
def hello():
    """Return greeting message."""
    return "Hello, CI/CD World!"


@app.route("/health")
def health():
    """Health check endpoint."""
    return "OK"


@app.route("/version")
def version():
    """Return application version."""
    return f"Version: {APP_VERSION}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 5000)))
