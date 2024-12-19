def save_table_text(table, filename):
    """
    Сохраняет таблицу в текстовом формате.
    Вывод будет аналогичен выводу на экран с использованием print_table().
    """
    if not table:
        raise ValueError("Таблица не может быть пустой.")

    # Проверим, что все столбцы имеют одинаковую длину
    num_rows = len(next(iter(table.values())))
    if not all(len(values) == num_rows for values in table.values()):
        raise ValueError("Все столбцы должны иметь одинаковое количество строк.")

    # Записываем текстовое представление таблицы
    with open(filename, 'w', encoding='utf-8') as f:
        # Заголовки столбцов
        headers = list(table.keys())
        f.write("\t".join(headers) + "\n")

        # Данные строк
        for i in range(num_rows):
            row = [table[col][i] for col in headers]
            f.write("\t".join(row) + "\n")
