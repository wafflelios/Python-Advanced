import time

from flask import Flask

app: Flask = Flask(__name__)

STORAGE = {}
MONTHS = ('январе', 'феврале', 'марте', 'апреле', 'мае',
          'июне', 'июле', 'августе', 'сентябре', 'октябре', 'ноябре', 'декабре')


@app.route('/add/<date>/<int:number>')
def save_payment_info(date, number):
    global STORAGE
    time.strptime(date, '%Y%m%d')
    year, month, day = int(date[:4]), int(date[4:6]), int(date[6:9])
    STORAGE.setdefault(year, {}).setdefault(month, {}).setdefault(day, 0)
    STORAGE[year][month][day] += number
    return f'{day}.{month}.{year} вы потратили {STORAGE[year][month][day]} рублей.'


@app.route('/calculate/<int:year>')
def payment_year(year):
    global STORAGE
    spending = 0
    STORAGE.setdefault(year, {})
    months = STORAGE[year]
    for key, value in months.items():
        spending += sum(value.values())
    return f'В {year} году вы потратили {spending} рублей.'


@app.route('/calculate/<int:year>/<int:month>')
def payment_month(year, month):
    spending = sum(STORAGE.setdefault(year, {}).setdefault(month, {}).values())
    return f'В {MONTHS[month - 1]} {year}-го года вы потратили {spending} рублей.'


if __name__ == "__main__":
    app.run(debug=True)
