# ������ 4.2.PP4E\System\Filetools\commands.py

#!/usr/local/bin/python
from sys import argv
from scanfile import scaner
class UnkownCommand(Exception): pass

def processLine(line):                # ���������� �������,
    if line[0] == '*':                # ����������� � ������ ������
        print("Ms, ", line[1:-1])
    elif line[0] == '+':
        print("Mr. ", line[1:-1])     # ��������� ������ � ��������� �������
    else:
        raise UnkownCommand(line)     # ��������� ����������
filename = 'data.txt'
if len(argv) == 2: filename = argv[1] # �������� ��������� ������ � �������
scaner(filename, processLine)         # ����� ��������� ������
