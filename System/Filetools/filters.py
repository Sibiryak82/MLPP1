# Пример 4.3.PP4E\System\Filetools\filters.py

import sys

def filter_files(name, function):       # фильтрация файлов через функцию
    input = open(name, 'r')             # создать объекты
    output = open(name + 'out', 'w')    # выходной файл
    for line in input:
        output.write(function(line))    # записать измененную строку
    input.close()
    output.close()                      # выходной файл имеет расширение '.out'

def filter_stream(function):            # отсутвуют явные файлы
    while True:                         # использовать стандартные потоки
        line = sys.readline()           # или: input()
        if not line: break
        print(function(line), end='')   # или: sys.stdout.write()

if __name__ == '__main__':
    filter_stream(lambda line: line)    # копировать stdin в stdout, если
                                        # запущен как самостоятельный сценарий