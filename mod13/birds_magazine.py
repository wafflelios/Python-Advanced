import sqlite3
import datetime
# -*- coding: utf-8 -*-

def check_if_such_bird_already_seen(cursor: sqlite3.Cursor, bird_name: str) -> bool:
    result = cursor.execute('SELECT EXISTS(SELECT 1 FROM table_birds WHERE bird_name = ? LIMIT 1)',
                            (bird_name,)).fetchone()[0]
    return bool(result)

def log_bird(cursor: sqlite3.Cursor, bird_name: str, date_time: str):
    cursor.execute('INSERT INTO table_birds (bird_name, date_time) VALUES (?, ?)', (bird_name, date_time))


if __name__ == '__main__':
    print('Выполняется программа ЮНат v0.1.')
    with sqlite3.connect('hw.db') as data_base:
        cursor = data_base.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS table_birds('
                       'id INTEGER PRIMARY KEY AUTOINCREMENT,'
                       'bird_name TEXT NOT NULL,'
                       'date_time TEXT NOT NULL)')
        bird_name = input('Введите имя птицы: ')
        if not check_if_such_bird_already_seen(cursor, bird_name):
            log_bird(cursor, bird_name, str(datetime.datetime.now()))
            print(f'Информация о птице {bird_name} была добавлена в журнал.')
        else:
            date_time = cursor.execute('SELECT * FROM table_birds WHERE bird_name = ?', (bird_name, )).fetchall()[0][2]
            print(f'Вы уже встречали данную птицу!\nДата и время встречи: {date_time}')

