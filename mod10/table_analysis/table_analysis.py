import sqlite3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    with sqlite3.connect('hw_3_database.db') as data_base:
        cursor = data_base.cursor()
        for num in range(1, 4):
            answer = cursor.execute(f'SELECT COUNT(*) FROM table_{num}').fetchall()[0][0]
            print(f'В таблице table_{num} хранится {answer} строк.')

        answer = cursor.execute(f'SELECT COUNT(DISTINCT value) FROM table_1').fetchall()[0][0]
        print(f'\nВ таблице table_1 {answer} уникальных записей.')

        answer = cursor.execute(f'SELECT COUNT(*) FROM table_1 '
                                f'WHERE value IN(SELECT value FROM table_2)').fetchall()[0][0]
        print(f'\nВ таблице table_2 встречается {answer} записей из таблицы table_1.')

        answer = cursor.execute(f'SELECT COUNT(*) FROM table_1 WHERE value IN(SELECT value FROM table_2) '
                                f'AND value IN(SELECT value FROM table_3)').fetchall()[0][0]
        print(f'\nВ таблице table_2 и table_3 встречается {answer} записей из таблицы table_1.')
