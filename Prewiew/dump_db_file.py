# Пример 1.3. PP4E\Preview\dump_db_file.py/

from make_db_file import loadDbase
db = loadDbase()
for key in db:
    print(key, '=>\n ', db[key])
print(db['sue']['name'])
