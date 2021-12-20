# Пример 5.16.PP4E\System\Exits\testexit_os.py

def outahere():
    import os
    print('Bye os world')
    os._exit(99)
    print('Never reached')

if __name__ == '__main__': outahere()