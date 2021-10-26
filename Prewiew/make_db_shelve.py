# Пример 1.11.PP4E\Preview\make_db_shelve.py

"""
Этот сценарий создаст в текущем каталоге один или более файлов,
имена которых начинаются с префикса people-shelve (в ОС Windows, под
управлением Python 3.1, сценарий создаст файлы people-shelve.bak,
people-shelve.dat и people-shelve.dir). Вы не должны удалять эти файлы
(они составляют вашу базу данных!), а чтобы получить доступ к этому
хранилищу в других сценариях, необходимо использовать то же самое
имя базы.
"""

from Prewiew.initdata import bob, sue, tom
import shelve
db = shelve.open('people-shelve')
db['bob'] = bob
db['sue'] = sue
db['tom'] = tom
db.close()