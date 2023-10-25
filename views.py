from flask import Blueprint, render_template, request, jsonify
from scraper import scraper
import validators

views = Blueprint(__name__, 'views')


@views.route('/api/scrape', methods=['POST'])
def scrape():
    request_data = request.json

    if 'url' not in request_data:
        return {'errorMessage': 'No URL provided'}, 400

    if not validators.url(request_data['url']):
        return {'errorMessage': 'Invalid URL'}, 400

    try:
        scraped_data = scraper(request_data['url'])
        return {'message': 'Scraping completed.', 'data': scraped_data}
    except Exception as e:
        return {'errorMessage': 'An error occured during scraping', 'error': str(e)}, 500
