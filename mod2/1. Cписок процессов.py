import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROCESS_FILE = os.path.join(BASE_DIR, 'output_file.txt')


def get_summary_rss(file_path):
    with open(file_path, 'r') as file:
        memory = sum(int(line.split()[5]) for line in file.readlines()[1:])
        inf_units = ['Кб', 'Мб', 'Гб', 'Тб', 'Пб', 'Эб', 'Зб', 'Йб']
        print(f'{memory} байт')
        for counter in range(1, 9):
            print(f'{memory / pow(1024, counter)} {inf_units[counter - 1]}')


get_summary_rss(PROCESS_FILE)
