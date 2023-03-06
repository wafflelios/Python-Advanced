import os
import sys


def get_mean_size():
    data = sys.stdin.readlines()
    if data:
        summa, counter = 0, 0
        for file in data:
            base_dir = os.path.dirname(os.path.abspath(__file__))
            path = os.path.join(base_dir, file[:-1])
            if os.path.isfile(path):
                stats = os.stat(path)
                summa += stats.st_size
                counter += 1
        print(f'Средний размер файла в каталоге: {summa / counter}')
    else:
        print('Либо в каталоге нет файлов, либо не удается получить их размер.')


get_mean_size()
