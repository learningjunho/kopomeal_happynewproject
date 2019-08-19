import requests

meal = None

def get_page(url):
    return requests.get(url).text

'''
다음과 같은 형식의 리스트로 학식 정보를 리턴함
[
    [월요일아침, 월요일점심, 월요일저녁]
    [화요일아침, 화요일점심, 화요일저녁]
    이하생략
]
'''
def parse_page(html):
    table = html.find('<table class="tbl_table menu">')
    tbody = html.find('<tbody>', table)

    start = tbody
    meal = []
    for i in range(7):
        meal.append([])
        for j in range(3):
            start = html.find("<span>",start)
            end = html.find("</span>",start)
            meal[i].append(html[start+6:end])
            start = end
    return meal

def get_meal():
    global meal
    if meal == None:
        html = get_page("http://www.kopo.ac.kr/anseong/content.do?menu=3295")
        meal = parse_page(html)
    return meal

# for debugging
def get_cached_meal():
    return meal