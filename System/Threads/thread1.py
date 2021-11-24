# Пример 5.5.PP4E\System\Threads\thread1.py
"порождает потоки выполнения, пока не будет нажата клавища 'q'"

import _thread

def child(tid):
    print('Hello from thread', tid)

def parent():
    i = 0
    while True:
        i += 1
        _thread.start_new_thread(child, (i,))
        if input() == 'q': break

parent()