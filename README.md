# Новое русское вино

Сайт магазина авторского вина "Новое русское вино".

## Установка
- Установите зависимости 
- ```pip install requirements```
- Заполните файл wine3.xlsx нужными Вам данными по шаблону и разместите его в корне:

| Категория     | Название            | Сорт            | Цена | Картинка                 | Акция                |
|---------------|---------------------|-----------------|------|--------------------------|----------------------|
| Белые вина    | Белая леди          | Дамский пальчик | 399  | belaya_ledi.png          | Выгодное предложение |
| Напитки       | Коньяк классический | Cell 6          | 350  | konyak_klassicheskyi.png |                      |
| Красные вина  | Ркацители           | Ркацители       | 499  | rkaciteli.png            |                      |

- Имя своего файла можно указать в файле .env в параметре `FILE`

## Запуск

- Скачайте код

- Запустите сайт командой 
- ```python3 main.py```
- Запуск с параметрами     
- ```python3 main.py -f filename.xlsx```
- Перейдите на сайт по адресу [http://127.0.0.1:8000](http://127.0.0.1:8000).

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).
