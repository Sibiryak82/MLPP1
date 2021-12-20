# Пример 5.17.PP4E\System\Exits\testexit_fork.py
"""
порождает дочерние процессы и получает коды их завершения вызовом функции
os.wait; прием ветвления может использоваться в Unix и Cygwin, но он не работает
в стандартной версии Python 3.1 для Windows;
примечание: порождаемые потоки выполнения совместно используют глобальные
переменные, но каждый процесс имеет собственные копии этих переменных (однако
при ветвлении процессов файловые дескрипторы используются совместно) --
exitstat здесь всегда имеет одно и то же значение, но может отличаться в случае
использования потоков;
"""
import os
exitstat = 0

def child():                    # здесь можно вызвать os.exit для заврешения
    global exitstat             # изменит глобальную переменную этого процесса
    exitstat += 1               # код завершения для функции wait родителя
    print('Hello from child', os.getpid(), exitstat)
    os._exit(exitstat)
    print('never reached')

def parent():
    while True:
        newpid = os.fork()     # запустить новую копию процесса
        if newpid == 0:        # если это копия, вызвать функцию child
            child()            # ждать ввода 'q' с консоли
        else:
            pid, status = os.wait()
            print('Parent got', pid, status, (status >> 8))
            if input() == 'q': break

        if __name__ == '__main__': parent()