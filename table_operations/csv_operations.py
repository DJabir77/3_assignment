import csv


def load_table_csv(filename):
    """
    Загружает таблицу из CSV файла в виде словаря.
    Каждый столбец будет представлен списком значений.
    """
    table = {}
    with open(filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            for key, value in row.items():
                if key not in table:
                    table[key] = []
                table[key].append(value)
    return table


def save_table_csv(table, filename):
    """
    Сохраняет таблицу (словарь) в CSV файл.
    """
    if not table:
        raise ValueError("Таблица не может быть пустой.")

    fieldnames = list(table.keys())
    with open(filename, mode='w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        num_rows = len(next(iter(table.values())))  # Количество строк (по одному столбцу)
        for i in range(num_rows):
            row = {key: table[key][i] for key in fieldnames}
            writer.writerow(row)
