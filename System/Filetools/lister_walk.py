# ѕример 4.4.PP4E\System\Filetools\lister_walk.py
"выводит список файлов в дереве каталогов с помощью os.walk"

import sys, os

def lister(root):                                        #  дл€ корневого каталога
    for (thisdir, subshere, fileshere) in os.walk(root)  # перечисл€ет
        print('[' + thisdir + ']')                       #  каталоги в дереве
        for fname in fileshere:                          # вывод файлов в каталоге
            path = os.path.join(thisdir, fname)          # добавить им€ каталога
            print(path)

if __name__ == '__main__':
    lister(sys.argv[1])                                  # командной строке
