import sqlite3

if __name__ == '__main__':
    with sqlite3.connect('hw_2_database.db') as data_base:
        cursor = data_base.cursor()
        with open('report.md', 'w') as report:
            answer = cursor.execute('SELECT * FROM table_checkout ORDER BY sold_count DESC').fetchone()
            report.write(f'# Результат исследования продаж телефонов\n\nЧаще всего покупают телефон цвета '
                         f'<b>{answer[0]}</b>.<br>Количество проданных телефонов: <b>{answer[1]}</b><br><br>')
            red_and_blue = cursor.execute('SELECT * FROM table_checkout WHERE phone_color IN ("Red", "Blue")'
                                          'ORDER BY sold_count DESC').fetchall()
            if red_and_blue[0][1] == red_and_blue[1][1]:
                report.write(f'Телефоны красного и синего цвета покупают с <b>одинаковой частотой</b>.\n\n')
            else:
                report.write(f'<b>Телефоны цвета {red_and_blue[0][0]} покупают чаще</b>, '
                             f'чем цвета {red_and_blue[1][0]}.<br>')
            report.write(f'Количество проданных телефонов цвета {red_and_blue[0][0]}: <b>{red_and_blue[0][1]}</b><br>'
                         f'Количество проданных телефонов цвета {red_and_blue[1][0]}: '
                         f'<b>{red_and_blue[1][1]}</b><br><br>')
            answer = cursor.execute('SELECT * FROM table_checkout ORDER BY sold_count').fetchone()
            report.write(f'Самый непопулярный цвет телефона: <b>{answer[0]}</b>'
                         f'<br>Количество проданных телефонов: <b>{answer[1]}</b>')
