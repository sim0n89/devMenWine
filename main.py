import os
import pprint
from collections import defaultdict
from http.server import HTTPServer, SimpleHTTPRequestHandler
from datetime import date
from jinja2 import Environment, FileSystemLoader, select_autoescape
import pandas
import argparse
from os.path import join, dirname
from dotenv import load_dotenv


def get_years(eyars_old):
    if eyars_old % 10 == 1 and eyars_old != 11 and eyars_old % 100 != 11:
        return f'{eyars_old} год'
    elif 1 < eyars_old % 10 <= 4 and eyars_old != 12 and eyars_old != 13 and eyars_old != 14:
        return f'{eyars_old} года'
    else:
        return f'{eyars_old} лет'


def main():
    dotenv_path = join(dirname(__file__), '.env')
    load_dotenv(dotenv_path)

    parser = argparse.ArgumentParser(
        description='Введите файл для загрузки товаров'
    )
    parser.add_argument('-f', '--file', help='Ваш файл', default="wine.xlsx")
    args = parser.parse_args()

    try:
        file = os.environ["FILE"]
    except KeyError:
        file = args.file

    excel_data = pandas.read_excel(file, na_filter=False)
    wines = excel_data.to_dict(orient='records')
    categories = defaultdict(list)
    for wine in wines:
        categories[wine['Категория']].append(wine)
    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )

    template = env.get_template('wine.html')
    years_old_text = get_years(date.today().year - 1920)
    rendered_page = template.render(
        years_old=years_old_text,
        categories=categories
    )

    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)

    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()


if __name__ == '__main__':
    main()
