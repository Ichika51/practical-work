"""Flask application for CI/CD demonstration."""
from flask import Flask

app = Flask(__name__)
APP_VERSION = "1.0.1"


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
    app.run(host="0.0.0.0", port=5000)
