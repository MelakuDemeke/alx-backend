#!/usr/bin/env python3
"""Flask app to server hello world"""
from flask import Flask, render_template, request
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

@babel.localeselector
def get_locale():
    """Get locale language from request"""
    return request.accept_languages.best_match(app.config_class.LANGUAGES)

@app.route('/')
def index():
    """index page of the app"""
    return render_template('3-index.html')

if __name__ == '__main__':
    app.run(debug=True)
