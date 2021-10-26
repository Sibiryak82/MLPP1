# Пример 1.22.PP4E\Preview\peopleinteract_update.py

"""
Сценарий в примере 1.22 является следующим шагом к созданию
интерфейса, позволяющим вносить изменения в интерактивном режиме.
Для заданного ключа он позволяет ввести значения для каждого
из полей и либо изменяет существующую запись, либо создает новую, после
чего сохраняет ее с указанным ключом.
"""

# интерактивные изменения
import shelve
from person import Person
fieldnames = ('name', 'age', 'job', 'pay')

db = shelve.open('class-shelve')
while True:
    key = input('\nKey? =>')
    if not key: break
    if key in db:
        record = db[key]                    # изменить существующую
    else:                                   # или создать новую запись
        record = Person(name='?', age='?')  # для eval: строки в кавычках
    for field in fieldnames:
        currval = getattr(record, field)
        newtext = input('\t[%s]=%s\n\t\tnew?=>' % (field, currval))
        if newtext:
            setattr(record, field, eval(newtext))
    db[key] = record
db.close()
