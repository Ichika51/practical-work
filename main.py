from flask import Flask

app = Flask(__name__)

APP_VERSION = "1.0.0"

@app.route('/')
def hello():
    return "Hello, CI/CD World!"

@app.route('/health')
def health():
    return "OK", 200

@app.route('/version')
def version():
    return f"Version: {APP_VERSION}", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)