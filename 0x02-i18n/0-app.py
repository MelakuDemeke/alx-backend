#!/usr/bin/env python3
"""Flask app to server hello world"""
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    """index page of the app"""
    return render_template('0-index.html')

if __name__ == '__main__':
    app.run(debug=True)
