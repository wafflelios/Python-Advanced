from flask import Flask
from random import choice
from datetime import datetime, timedelta
import re
import os

app = Flask(__name__)

CARS = ['Chevrolet', 'Renault', 'Ford', 'Lada']
CATS = ['корниш-рекс', 'русская голубая', 'шотландская вислоухая', 'мейн-кун', 'манчкин']

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BOOK_FILE = os.path.join(BASE_DIR, 'war_and_peace.txt')

VISITS = 0

with open(BOOK_FILE, encoding='windows-1251') as book:
    opened_book = book.read()
    words = re.findall(r"\w+'\w+|[^\W\d]+", opened_book)


@app.route('/hello_world')
def hello_world():
    return 'Привет, мир!'


@app.route('/cars')
def cars():
    return ", ".join(CARS)


@app.route('/cats')
def cats():
    return choice(CATS)


@app.route('/get_time/now')
def now():
    return 'Точное время: {current_time}'.format(current_time=str(datetime.now()).split()[-1])


@app.route('/get_time/future')
def future():
    hours, minutes, seconds = str(datetime.now()).split()[-1].split(':')
    hours, minutes, seconds = int(hours), int(minutes), float(seconds)
    return 'Точное время через час будет: {current_time_after_hour}'.format(current_time_after_hour=timedelta(
        hours=hours, minutes=minutes, seconds=seconds) + timedelta(hours=1))


@app.route('/get_random_word')
def word():
    return choice(words)


@app.route('/counter')
def counter():
    global VISITS
    VISITS += 1
    return str(VISITS)
