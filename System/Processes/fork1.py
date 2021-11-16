# Пример 5.1.PP4E\System\Processes\fork1.py
"ответвляет дочерние процессы, пока не будет нажата клавиша 'q'"

import os

def child():
    print('Hello from child', os.getpid())
    os._exit(0)   # иначе пройзойдет возврат в родительский цикл

def parent():
    while True:
        newpid = os.fork()
        if newpid == 0:
            child()
        else:
            print('Hello from parent', os.getpid(), newpid)
        if input() == 'q': break

parent()