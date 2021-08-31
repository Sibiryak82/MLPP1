# Пример 1.21.PP4E\Preview\peopleinteract_query.py

"""
Сценарий в примере 1.21 реализует простейший
цикл интерактивных взаимодействий, позволяя пользователю
запрашивать объекты, имеющиеся в хранилище.
"""

# интерактивные запросы

import shelve


fieldnames = ('name', 'age', 'job', 'pay')
maxfield = max(len(f) for f in fieldnames)
db = shelve.open('class-shelve')


while True:
    key = input('\nKey? => ')   # ключ или пустая срока, возбуждает исключение

    if not key: break
    try:
        record = db[key]       # извлечь запись по ключу и вывести
    except:
        print('No such key "%s"!' % key)
    else:
        for field in fieldnames:
            print(field.ljust(maxfield), '=>', getattr(record, field))


