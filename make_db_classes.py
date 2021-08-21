# Пример 1.18.PP4E/Preview/make_db_classes.py

"""
Этот сценарий создает три экземпляра (два экземпляра оригинально-
го класса и один – его специализированной версии) и присваивает их
ключам вновь созданного хранилища. Другими словами, сценарий соз-
дает хранилище с экземплярами классов. Для нашего программного
кода база выглядит в точности, как словарь экземпляров классов, с той
лишь разницей, что словарь верхнего уровня отображается в файл хра-
нилища, как и прежде
"""

import shelve
from person import Person
from manager import Manager

bob = Person('Bob Smith', 42, 30000, 'software')
sue = Person('Sue Jones', 45, 40000, 'hardware')
tom = Manager('Tom Doe', 50, 50000)

db = shelve.open('class-shelve')
db['bob'] = bob
db['sue'] = sue
db['tom'] = tom
db.close()