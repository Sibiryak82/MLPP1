# Пример 1.10.PP4E\Preview\update_db_pickle_recs.py

"""
Cценарий в примере 1.10 обновляет содержимое базы данных,
извлекая запись из ее файла, изменяя объект в памяти и затем
сохраняя его обратно в файл с помощью модуля pickle.
На этот раз для внесения изменений необходимо извлечь и
сохранить единственную запись,
а не всю базу данных.
"""

import pickle
suefile = open('sue.pkl', 'rb')
sue = pickle.load(suefile)
suefile.close()
sue['pay'] *= 1.10
suefile = open('sue.pkl', 'wb')
pickle.dump(sue, suefile)
suefile.close()