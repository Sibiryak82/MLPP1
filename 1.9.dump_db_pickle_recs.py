# Пример 1.9.PP4E\Preview\dump_db_pickle_recs.py

import pickle, glob
for filename in glob.glob('*.pkl'):  # для 'bob', 'sue', 'tom'
    recfile = open(filename, 'rb')
    record = pickle.load(recfile)
    print(filename, '=>\n', record)

suefile = open('sue.pkl', 'rb')
print(pickle.load(suefile)['name'])  # извлечь имя Сью