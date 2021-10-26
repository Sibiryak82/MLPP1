# Пример 1.8.PP4E\Preview\make_db_pickle_recs.py

"""
Сценарий из примера 1.8 сохраняет каждую запись в отдельном файле, где в
качестве имени файла используется уникальный ключ записи, к которому добавляется расширение .pkl
(он создает файлы bob.pkl, sue.pkl и tom.pkl в текущем рабочем каталоге).
"""

from Prewiew.initdata import bob, sue, tom
import pickle
for(key, record) in [('bob', bob), ('tom', tom), ('sue', sue)]:
    recfile = open(key + '.pkl', 'wb')
    pickle.dump(record, recfile)
    recfile.close()