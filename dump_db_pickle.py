# Пример 1.6.PP4E\Preview\dump_db_pickle.py

import pickle
dbfile = open('people-pickle', 'rb')   # в версии 3.X следует использовать
db = pickle.load(dbfile)               # двоичный режим работы с файлами
for key in db:
    print(key, '=>\n ', db[key])
print(db['sue']['name'])