import sqlite3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    with sqlite3.connect('hw_4_database.db') as data_base:
        cursor = data_base.cursor()
        answer = cursor.execute('SELECT COUNT(*) FROM salaries WHERE salary < 5000').fetchone()[0]
        print(f'{answer} человек находятся за чертой бедности.')

        salary_mid = cursor.execute('SELECT AVG(salary) FROM salaries').fetchone()[0]
        print(f'Средняя зарплата по острову N составляет {salary_mid} рублей.')

        amount = cursor.execute('SELECT COUNT(*) FROM salaries').fetchall()[0][0]
        middle_1 = cursor.execute('SELECT salary FROM salaries ORDER BY salary DESC'
                                  ).fetchall()[amount // 2 - 1][0]
        middle_2 = cursor.execute('SELECT salary FROM salaries ORDER BY salary DESC'
                                  ).fetchall()[amount // 2][0]
        middle = (middle_1 + middle_2) / 2
        print(f'Медианная зарплата по острову равна {middle}.')

        full_sum = cursor.execute(f'SELECT SUM(salary) FROM salaries').fetchone()[0]
        rich_10 = cursor.execute(f'SELECT SUM(salary) FROM (SELECT * FROM salaries ORDER BY salary DESC '
                                 f'LIMIT {amount} * 0.1)').fetchone()[0]
        poor_90 = full_sum - rich_10
        answer = round(rich_10 / poor_90 * 100, 2)
        print(f'Число социального неравенства F равно {answer}%.')
