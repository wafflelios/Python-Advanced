import csv
import sqlite3


def delete_wrong_fees(cursor: sqlite3.Cursor, wrong_fees_file: str):
    with open(wrong_fees_file, 'r') as file:
        opened_file = list(csv.reader(file))[1:]
        for entry in opened_file:
            cursor.execute('DELETE FROM table_fees WHERE truck_number = ? AND timestamp = ?', (entry[0], entry[1]))


if __name__ == "__main__":
    with sqlite3.connect('hw.db') as data_base:
        cursor = data_base.cursor()
        delete_wrong_fees(cursor, "wrong_fees.csv")
