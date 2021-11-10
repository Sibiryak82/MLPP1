# Пример 1.19.PP4E\Preview\dump_db_classes.py

"""
В этом примере  не требуется импортировать класс Person, чтобы извлекать экземпляры
 из хранилища или вызывать их методы. Когда экземпляры сохраняются с помощью модуля
shelve или pickle, используемая этими модулями система сохранения
записывает в файл не только значения атрибутов экземпляров, но и
дополнительную информацию, позволяющую позднее автоматически
определить местоположение классов при извлечении экземпляров
(модули с определениями классов просто должны находиться в пути
поиска модулей при выполнении операции загрузки). Это сделано
специально, потому что определение класса и его экземпляры в хранилище
сохраняются отдельно; вы можете изменить класс, чтобы изменить
порядок интерпретации экземпляров при загрузке. Ниже приводятся результаты запуска
сценария dump_db_classes.py сразу после создания хранилища с помощью
сценария make_db_classes.py:
bob =>
Bob Smith 30000
sue =>
Sue Jones 40000
tom =>
Tom Doe 50000
Smith
Doe
"""

import shelve
db = shelve.open('class-shelve')
for key in db:
    print(key, '=>\n ', db[key].name, db[key].pay)

bob = db['bob']
print(bob.lastName())
print(db['tom'].lastName())