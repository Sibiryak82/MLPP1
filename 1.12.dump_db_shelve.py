# Пример 1.12.PP4E\Preview\dump_db_shelve.py

import shelve
db = shelve.open('people-shelve')
for key in db:
    print(key, '=>\n ', db[key])
print(db['sue']['name'])
db.close()