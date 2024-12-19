import pickle

def load_table_pickle(filename):
    """
    Загружает таблицу из Pickle файла.
    """
    with open(filename, 'rb') as f:
        table = pickle.load(f)
    return table

def save_table_pickle(table, filename):
    """
    Сохраняет таблицу (словарь) в Pickle файл.
    """
    with open(filename, 'wb') as f:
        pickle.dump(table, f)
