#!/usr/bin/env python3
"""Flask app to server hello world"""
from flask import Flask, render_template
from flask_babel import Babel

class Config:
    """Create a Flask Babel configuration."""
    LANGUAGES = ["en", "fr"]

app = Flask(__name__)
app.config_class = Config
app.config['LANGUAGES'] = Config.LANGUAGES
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['BABEL_DEFAULT_TIMEZONE'] = 'UTC'
babel = Babel(app)

@app.route('/')
def index():
    """index page of the app"""
    return render_template('1-index.html')

if __name__ == '__main__':
    app.run(debug=True)
