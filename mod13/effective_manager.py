import sqlite3
# -*- coding: utf-8 -*-

def get_a_raise_or_get_fired(cursor: sqlite3.Cursor, employee: str) -> None:
    sovin_salary = cursor.execute('SELECT salary FROM table_effective_manager WHERE name = "Иван Совин"').fetchone()[0]
    employee_salary = cursor.execute('SELECT salary FROM table_effective_manager WHERE name = ?',
                                     (employee, )).fetchone()
    if not employee_salary:
        print(f'Ошибка: Сотрудник {employee} не найден в базе данных.')
    elif employee == 'Иван Совин':
        print('Ошибка: Нельзя менять з/п эффективного менеджера.')
    else:
        increased_salary = int(employee_salary[0] * 1.1)
        if increased_salary > sovin_salary:
            cursor.execute('DELETE FROM table_effective_manager WHERE name = ?', (employee, ))
            print(f'Сотрудник {employee} был уволен!')
        else:
            cursor.execute('UPDATE table_effective_manager SET salary = ? WHERE name = ?', (increased_salary, employee))
            print(f'З/п сотрудника {employee} была повышена до {increased_salary}!')


if __name__ == '__main__':
    with sqlite3.connect('hw.db') as data_base:
        cursor = data_base.cursor()
        employee = input('Введите ФИО сотрудника в формате Фамилия И.О.: ')
        get_a_raise_or_get_fired(cursor, employee)