# Пример 1.12.PP4E\Preview\dump_db_shelve.py

"""Мы по-прежнему имеем словарь словарей, но на этот раз словарем верхнего уровня является хранилище, отображаемое в файл. Всякий раз,
когда происходит обращение к элементу в хранилище, модуль shelve
выполняет необходимые операции с файловой системой, обеспечивающей доступ по ключу, и использует модуль pickle для сериализации
и десериализации объектов. Однако, с точки зрения программиста,
хранилище – это всего лишь словарь, обладающий возможностью сохраняться между вызовами программы
"""

import shelve
db = shelve.open('people-shelve')
for key in db:
    print(key, '=>\n ', db[key])
print(db['sue']['name'])
db.close()