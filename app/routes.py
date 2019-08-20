from flask import render_template
from app import app
from app import crawl
import datetime

meal = None

@app.route('/')
@app.route('/index')
def index():
    global meal
    meal = crawl.get_meal()
    now = datetime.datetime.now()
    today_meal = meal[now.weekday()]
    return render_template('index.html', meal = meal, today_meal = today_meal)

@app.route('/debug')
def debug():
    cached_meal = crawl.get_cached_meal()
    return render_template("debug.html", meal = meal, cached_meal = cached_meal, lastcrawl = crawl.lastcrawl, nextcrawl = crawl.nextcrawl)