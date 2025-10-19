# app.py
# ------------------------------
# Simple Python web app using Flask.
# Deployed automatically using GitHub Actions (without Docker).
# ------------------------------

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from GitHub Actions CI/CD Pipeline without Docker!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
