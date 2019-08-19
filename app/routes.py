from flask import render_template
from app import app
from app import crawl
import datetime

meal = crawl.get_meal()
now = datetime.datetime.now()
today_meal = meal[now.weekday()]

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', meal = meal, today_meal = today_meal)

@app.route('/debug')
def debug():
    cached_meal = crawl.get_cached_meal()
    return render_template("debug.html", meal = meal, now = now, cached_meal = cached_meal)