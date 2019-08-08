import requests

meal = None
lastcrawled = None

def get_page(url):
    return requests.get(url).text

def parse_page(html):
    table = html.find('<table class="tbl_table menu">')
    tbody = html.find('<tbody>', table)

    start = tbody
    meal = []
    for i in range(21):
        start = html.find("<span>",start)
        end = html.find("</span>",start)
        meal.append(html[start+6:end])
        start = end
    return meal

def get_meal():
    global meal
    if meal == None:
        html = get_page("http://www.kopo.ac.kr/anseong/content.do?menu=3295")
        meal = parse_page(html)
    return meal