import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from Flask CI/CD Demo!"

@app.route("/health")
def health():
    return {
        "status": "UP",
        "application": "flask-cicd-demo"
    }
@app.route("/config")
def config():
    return {
        "app": os.getenv("APP_NAME"),
        "environment": os.getenv("ENVIRONMENT")
    }
@app.route("/secret")
def secret():
    return {
        "password": os.getenv("DB_PASSWORD")
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
