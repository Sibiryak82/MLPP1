# Пример 1.4.PP4E\Preview\update_db_file.py

from Prewiew.make_db_file import loadDbase, storeDbase
db = loadDbase()
db['sue']['pay'] *= 1.10
db['tom']['name'] = 'Tom Tom'
storeDbase(db)