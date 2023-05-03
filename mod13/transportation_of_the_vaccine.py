import sqlite3


def check_if_vaccine_has_spoiled(cursor: sqlite3.Cursor, truck_number: str) -> bool:
    result = cursor.execute('SELECT COUNT(*) FROM(SELECT * FROM table_truck_with_vaccine WHERE truck_number = ? AND'
                            ' temperature_in_celsius NOT BETWEEN 16 AND 20)', (truck_number,)).fetchone()[0]
    return result >= 3

def check_if_truck_exists(cursor: sqlite3.Cursor, truck_number: str) -> bool:
    result = cursor.execute('SELECT EXISTS(SELECT 1 FROM table_truck_with_vaccine WHERE truck_number = ? LIMIT 1)',
                            (truck_number,)).fetchone()[0]
    return bool(result)


if __name__ == "__main__":
    with sqlite3.connect('hw.db') as data_base:
        cursor = data_base.cursor()
        truck_num = input('Введите номер грузовика: ')
        if check_if_truck_exists(cursor, truck_num):
            if check_if_vaccine_has_spoiled(cursor, truck_num):
                print(f'Вакцина в грузовике с номером {truck_num} была испорчена.')
            else:
                print(f'Вакцина в грузовике с номером {truck_num} не была испорчена.')
        else:
            print(f'Грузовика с номером {truck_num} нет в таблице.')
