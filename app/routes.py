from flask import render_template
from app import app
from app import crawl

meal = crawl.get_meal()

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', meal = meal)