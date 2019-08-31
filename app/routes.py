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
    try:
        tomorrow_meal = meal[now.weekday() + 1]
    except IndexError:
        tomorrow_meal = ["아직 확인되지 않았습니다.", "", ""]
    return render_template('index.html', meal = meal, today_meal = today_meal, tomorrow_meal = tomorrow_meal)

@app.route('/week')
def week():
    global meal
    meal = crawl.get_meal()
    return render_template('week.html', meal = meal)

@app.route('/debug')
def debug():
    cached_meal = crawl.get_cached_meal()
    return render_template("debug.html", meal = meal, cached_meal = cached_meal, lastcrawl = crawl.lastcrawl, nextcrawl = crawl.nextcrawl)

@app.route('/recrawl')
def recrawl():
    global meal
    meal = crawl.recrawl_meal()
    return "재크롤링 완료 <a href ='/debug'> 돌아가기 </a>  "