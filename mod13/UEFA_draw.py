import sqlite3
from random import choice
# -*- coding: utf-8 -*-

NOUNS = ['инженер', 'заказ', 'костюм', 'фронт', 'мешок', 'лидер', 'десяток', 'январь', 'ум',
         'самолет', 'учет', 'выбор', 'субъект', 'ноябрь', 'дом', 'момент', 'коллектив', 'поезд', 'метод',
         'друг', 'спектакль', 'час', 'прокурор', 'переход', 'дым', 'мужик', 'комплекс', 'анализ', 'майор', 'текст',
         'том', 'адрес']

ADJECTIVES = ['летний', 'отчаянный', 'минимальный', 'непривычный', 'интеллектуальный', 'колючий', 'президентский',
              'неудачный', 'любовный', 'смутный', 'промежуточный', 'коричневый', 'подробный', 'тупой', 'мясной',
              'приятный', 'теплый', 'негативный', 'общий', 'сумасшедший', 'британский', 'либеральный', 'напряженный',
              'публичный', 'тогдашний', 'желающий', 'эмоциональный', 'генетический', 'интересный', 'хрупкий',
              'патриотический', 'населенный', 'драматический']

COUNTRIES = ['Таиланд', 'Финляндия', 'Таджикистан', 'Уганда', 'Мадагаскар', 'Нигер', 'Тонга', 'Микронезия', 'Индия',
             'Австрия', 'Коста-Рика', 'Турция', 'Новая Зеландия', 'Ирландия', 'Южная Корея', 'Науру', 'Черногория',
             'Ливан', 'Доминиканская Республика', 'Индонезия', 'Палау', 'Казахстан', 'Эритрея', 'Мальта', 'Кувейт',
             'Мали', 'Малайзия', 'Северная Корея', 'Танзания', 'Конго', 'Греция', 'Кения']


def generate_test_data(cursor: sqlite3.Cursor, number_of_group: int) -> None:
    cursor.execute('DELETE FROM uefa_commands')
    cursor.execute('DELETE FROM uefa_draw')
    group_number, counter = 1, 0
    for team_id in range(number_of_group * 4):
        name = f'{choice(ADJECTIVES).title()} {choice(NOUNS)}'
        country = choice(COUNTRIES)
        if team_id % 4 == 0:
            level = 'Сильная'
        elif team_id % 4 in (1, 2):
            level = 'Средняя'
        else:
            level = 'Слабая'
        cursor.execute('INSERT INTO uefa_commands (command_number, command_name, command_country, command_level)'
                       'VALUES (?, ?, ?, ?)', (team_id + 1, name, country, level))
        if counter == 4:
            counter = 0
            group_number += 1
        cursor.execute('INSERT INTO uefa_draw (id, command_number, group_number) VALUES (?, ?, ?)',
                       (team_id + 1, team_id + 1, group_number))
        counter += 1


if __name__ == '__main__':
    with sqlite3.connect('hw.db') as data_base:
        cursor = data_base.cursor()
        number_of_group = int(input('Введите количество групп(от 4 до 16): '))
        generate_test_data(cursor, number_of_group)
