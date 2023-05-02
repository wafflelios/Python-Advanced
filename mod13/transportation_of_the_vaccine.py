import sqlite3
# -*- coding: utf-8 -*-


def check_if_vaccine_has_spoiled(cursor: sqlite3.Cursor, truck_number: str):
    result = cursor.execute('SELECT COUNT(*) FROM(SELECT * FROM table_truck_with_vaccine WHERE truck_number = ? AND'
                            ' temperature_in_celsius NOT BETWEEN 16 AND 20)', (truck_number, )).fetchone()[0]
    return result >= 3


if __name__ == "__main__":
    with sqlite3.connect('hw.db') as data_base:
        cursor = data_base.cursor()
        truck_num = input('Введите номер грузовика: ')
        print(check_if_vaccine_has_spoiled(cursor, truck_num))
