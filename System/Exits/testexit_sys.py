# Пример 5.15.PP4E\System\Exits\testexit_sys.py

def later():
    import sys
    print('Bye sys world')
    sys.exit(42)
    print('Never reached')

if __name__ == '__main__': later()