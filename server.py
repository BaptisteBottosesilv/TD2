from flask import Flask
from bs4 import BeautifulSoup
from datetime import datetime
pip install Flask-Caching
from flask import Flask
from flask_caching import Cache

app = Flask(__name__)
cache = Cache(app, config={'CACHE_TYPE': 'SimpleCache'})


@app.route('/get_latest_article_info')
@cache.cached(timeout=50)

def index():
     url = 'https://deepmind.google/discover/blog/'
     response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        last_article = soup.select_one('article_selector')
        author = last_article.select_one('author_selector').get_text(strip=True)
        date_published = last_article.select_one('date_selector').get_text(strip=True)
        return jsonify({
            'author': author,
            'date_published': date_published
        })
    else:
        return jsonify({'error': 'Failed to retrieve data'}), 500

    return ("Hello world")

if __name__ == '__main__':
    app.run()
