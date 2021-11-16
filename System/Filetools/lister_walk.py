# ������ 4.4.PP4E\System\Filetools\lister_walk.py
"������� ������ ������ � ������ ��������� � ������� os.walk"

import sys, os

def lister(root):                                        #  ��� ��������� ��������
    for (thisdir, subshere, fileshere) in os.walk(root)  # �����������
        print('[' + thisdir + ']')                       #  �������� � ������
        for fname in fileshere:                          # ����� ������ � ��������
            path = os.path.join(thisdir, fname)          # �������� ��� ��������
            print(path)

if __name__ == '__main__':
    lister(sys.argv[1])                                  # ��������� ������
