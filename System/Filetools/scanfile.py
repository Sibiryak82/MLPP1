# Пример 4.1.PP4E\System\Filetools\scanfile.py

def scanner(name, function):
    file = open(name, 'r')        # создать объект файла
    while True:
        line = file.readline()    # вызов методов файла
        if not line: break        # до конца файла
        function(line)            # вызвать объект функции
    file.close()