# Пример 4.2.PP4E\System\Filetools\commands.py

#!/usr/local/bin/python
from sys import argv
from scanfile import scaner
class UnkownCommand(Exception): pass

def processLine(line):                # определить функцию,
    if line[0] == '*':                # применяемую в каждой строке
        print("Ms, ", line[1:-1])
    elif line[0] == '+':
        print("Mr. ", line[1:-1])     # отбросить первый и последний символы
    else:
        raise UnkownCommand(line)     # возбудить исключение
filename = 'data.txt'
if len(argv) == 2: filename = argv[1] # аргумент командной строки с имененм
scaner(filename, processLine)         # файла запускает сканер
