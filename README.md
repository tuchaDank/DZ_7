# Домашнее задание №7 — Работа с API

Две программы на Python для работы с публичными API.

## Задание 1

`post.py` отправляет GET-запрос к JSONPlaceholder и выводит заголовки и тексты первых пяти постов.

## Задание 2

`weather.py` запрашивает название города, получает данные из OpenWeather API и выводит текущую температуру и описание погоды.

Для работы программы необходим API-ключ OpenWeather, переданный через переменную окружения `OPENWEATHER_API_KEY`.

## Установка


python3 -m pip install -r requirements.txt

## Запуск

Первое задание:


python3 post.py


Второе задание (Linux):


export OPENWEATHER_API_KEY="ваш_api_ключ"
python3 weather.py

