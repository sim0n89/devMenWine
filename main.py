from collections import defaultdict
from http.server import HTTPServer, SimpleHTTPRequestHandler
import datetime
from jinja2 import Environment, FileSystemLoader, select_autoescape
import pandas
import pprint


def get_years(eyars_old):
    if eyars_old % 10 == 1 and eyars_old != 11 and eyars_old % 100 != 11:
        return f'{eyars_old} год'
    elif 1 < eyars_old % 10 <= 4 and eyars_old != 12 and eyars_old != 13 and eyars_old != 14:
        return f'{eyars_old} года'
    else:
        return f'{eyars_old} лет'


excel_data = pandas.read_excel('wine3.xlsx', na_filter=False)
wines = excel_data.to_dict(orient='records')
categories = defaultdict(list)
for wine in wines:
    categories[wine['Категория']].append(wine)

pprint.pprint(categories)
env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html', 'xml'])
)
delta = (datetime.datetime.now() - datetime.datetime(year=1920, month=1, day=1))
years = delta.days // 365
template = env.get_template('wine.html')
yers_old = get_years(years)
rendered_page = template.render(
    years_old=yers_old,
    categories=categories
)

with open('index.html', 'w', encoding="utf8") as file:
    file.write(rendered_page)

server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
server.serve_forever()
