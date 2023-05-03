import sqlite3
from datetime import date, timedelta, datetime
from random import choice
# -*- coding: utf-8 -*-

TRAININGS = ['футбол', 'хоккей', 'шахматы', 'SUP-сёрфинг', 'бокс', 'Dota2', 'шахбокс']

def update_work_schedule(cursor: sqlite3.Cursor, year: int) -> None:
    cursor.execute('DELETE FROM table_friendship_schedule')
    workers = []
    for week_id in range(7):
        preferable_sport = TRAININGS[week_id]
        available_workers = cursor.execute('SELECT * FROM table_friendship_employees WHERE preferable_sport != ?',
                                           (preferable_sport, )).fetchall()
        workers.append(available_workers)
    current_date = date(year, 1, 1)
    while current_date != date(year + 1, 1, 2):
        for _ in range(10):
            worker = choice(workers[datetime.weekday(current_date)])
            cursor.execute('INSERT INTO table_friendship_schedule (employee_id, date) VALUES(?, ?)',
                       (worker[0], current_date))
        current_date += timedelta(days=1)
    print(f'Расписание на {year} год было составлено!')


if __name__ == '__main__':
    with sqlite3.connect('hw.db') as data_base:
        cursor = data_base.cursor()
        year = int(input('Введите год, на который нужно составить расписание: '))
        update_work_schedule(cursor, year)
