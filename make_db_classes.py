# Пример 1.18.PP4E\Preview\make_db_classes.py

"""Мы могли
бы снова сохранять каждую запись в отдельном файле с помощью модуля
 pickle, но модуль shelve предоставляет точно такую же возможность,
а кроме того, его гораздо проще использовать. Как это сделать,
демонстрируется в примере 1.18.
"""

import shelve
from person import Person
from manager import Manager

bob = Person('Bob Smith', 42, 30000, 'software')
sue = Person('Sue Jones', 45, 40000, 'hardware')
tom = Manager('Tom Doe', 50, 50000,)

db = shelve.open('class-shelve')
db['bob'] = bob
db['sue'] = sue
db['tom'] = tom
db.close()