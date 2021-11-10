# ������ 4.3.PP4E\System\Filetools\filters.py

import sys

def filter_files(name, function):       # ���������� ������ ����� �������
    input = open(name, 'r')             # ������� �������
    output = open(name + 'out', 'w')    # �������� ����
    for line in input:
        output.write(function(line))    # �������� ���������� ������
    input.close()
    output.close()                      # �������� ���� ����� ���������� '.out'

def filter_stream(function):            # ��������� ����� �����
    while True:                         # ������������ ����������� ������
        line = sys.readline()           # ���: input()
        if not line: break
        print(function(line), end='')   # ���: sys.stdout.write()

if __name__ == '__main__':
    filter_stream(lambda line: line)    # ���������� stdin � stdout, ����
                                        # ������� ��� ��������������� ��������