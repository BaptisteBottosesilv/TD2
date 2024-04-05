from flask import Flask
from bs4 import BeautifulSoup
from datetime import datetime
pip install Flask-Caching
from flask import Flask
from flask_caching import Cache

app = Flask(__name__)
cache = Cache(app, config={'CACHE_TYPE': 'SimpleCache'})


@app.route('/https://deepmind.google/discover/blog/tacticai-ai-assistant-for-football-tactics/')
@cache.cached(timeout=50)

def index():

    return ("Hello world")

if __name__ == '__main__':
    app.run()
