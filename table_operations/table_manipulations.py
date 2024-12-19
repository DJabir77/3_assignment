# table_manipulations.py

def get_rows_by_number(start, stop, table):
    """
    Получение строк таблицы по номерам.
    """
    if not table:
        raise ValueError("Таблица не может быть пустой.")
    rows = list(table.values())[start:stop]
    return rows


def get_rows_by_index(*names, table):
    """
    Получение строк таблицы по именам в первой колонке.
    """
    if not table:
        raise ValueError("Таблица не может быть пустой.")
    rows = []
    for row in zip(*table.values()):
        if row[0] in names:  # Проверка, что имя из первой колонки присутствует
            rows.append(row)
    return [dict(zip(table.keys(), row)) for row in rows]


def get_column_types(table):
    """
    Получение типов данных каждого столбца.
    """
    return {i: type(val[0]) for i, val in table.items()}


def set_column_types(types_dict, table):
    """
    Установка типов для столбцов.
    """
    if not table:
        raise ValueError("Таблица не может быть пустой.")

    for col_name, col_type in types_dict.items():
        if col_name not in table:
            raise KeyError(f"Столбец с именем '{col_name}' не найден в таблице.")
        table[col_name] = [col_type(val) for val in table[col_name]]


def get_value(column, table, by_number=False):
    """
    Получение одного значения из указанного столбца.
    """
    values = get_values(column, table, by_number)  # Используем уже определенную функцию get_values
    if not values:
        raise ValueError(f"Не найдено значений для столбца {column}.")
    return values[0]  # Возвращаем первое значение (если требуется только одно значение)



def set_values(values, column_name, table):
    """
    Установка значений столбца по имени.
    """
    if not table:
        raise ValueError("Таблица не может быть пустой.")

    if column_name not in table:
        raise KeyError(f"Столбец с именем '{column_name}' не найден в таблице.")

    if len(values) != len(table[column_name]):
        raise ValueError("Количество значений не совпадает с количеством строк в столбце.")

    table[column_name] = values


def set_value(value, column_name, table):
    """
    Установка одного значения в столбец.
    """
    if not table:
        raise ValueError("Таблица не может быть пустой.")

    if column_name not in table:
        raise KeyError(f"Столбец с именем '{column_name}' не найден в таблице.")

    table[column_name] = [value] * len(table[column_name])


def print_table(table):
    """
    Печать таблицы.
    """
    if not table:
        raise ValueError("Таблица не может быть пустой.")

    print("\t".join(table.keys()))
    for row in zip(*table.values()):
        print("\t".join(str(val) for val in row))


def set_values(values, column, table, by_number=False):
    """
    Установка значений указанного столбца таблицы.
    """
    if not table:
        raise ValueError("Таблица не может быть пустой.")

    if by_number:
        if isinstance(column, int):
            if column < 0 or column >= len(table):
                raise IndexError(f"Индекс столбца {column} вне диапазона.")
            column_name = list(table.keys())[column]
        else:
            raise ValueError("Ожидался индекс столбца, а не имя столбца.")
    else:
        column_name = column
        if column_name not in table:
            raise KeyError(f"Столбец с именем '{column_name}' не найден в таблице.")

    if len(values) != len(table[column_name]):
        raise ValueError("Количество значений не совпадает с количеством строк в таблице.")

    table[column_name] = values


def set_values(values, column, table, by_number=True):
    """
    Устанавливает значения для указанного столбца таблицы.
    """
    if not table:
        raise ValueError("Таблица не может быть пустой.")

    if by_number:
        if isinstance(column, int):
            if column < 0 or column >= len(table):
                raise IndexError(f"Индекс столбца {column} вне диапазона.")
            column_name = list(table.keys())[column]
        else:
            raise ValueError("Ожидался индекс столбца, а не имя столбца.")
    else:
        column_name = column
        if column_name not in table:
            raise KeyError(f"Столбец с именем '{column_name}' не найден в таблице.")

    if len(values) != len(table[column_name]):
        raise ValueError(
            f"Количество значений ({len(values)}) не совпадает с количеством строк в таблице ({len(table[column_name])}).")

    table[column_name] = values


def set_value(value, column, table, by_number=False):
    """
    Установка значения в ячейку столбца. Можно указать индекс столбца или его имя.
    """
    if not table:
        raise ValueError("Таблица не может быть пустой.")

    if by_number:
        if isinstance(column, int):
            if column < 0 or column >= len(table):
                raise IndexError(f"Индекс столбца {column} вне диапазона.")
            column_name = list(table.keys())[column]
        else:
            raise ValueError("Ожидался индекс столбца, а не имя столбца.")
    else:
        column_name = column
        if column_name not in table:
            raise KeyError(f"Столбец с именем '{column_name}' не найден в таблице.")

    # Установка значения в соответствующем столбце
    for i in range(len(table[column_name])):
        table[column_name][i] = value


def get_values(column, table, by_number=False):
    """
    Получение значений указанного столбца таблицы.
    Если by_number=True, передается индекс столбца (нумерация с 0),
    если by_number=False — передается имя столбца.
    """
    if not table:
        raise ValueError("Таблица не может быть пустой.")

    if by_number:
        if isinstance(column, int):
            if column < 0 or column >= len(table):
                raise IndexError(f"Индекс столбца {column} вне диапазона.")
            column_name = list(table.keys())[column]
        else:
            raise ValueError("Ожидался индекс столбца, а не имя столбца.")
    else:
        column_name = column
        if column_name not in table:
            raise KeyError(f"Столбец с именем '{column_name}' не найден в таблице.")

    return table[column_name]


def print_table(table):
    """
    Выводит таблицу в виде красивой таблицы с заголовками.
    """
    if not table:
        raise ValueError("Таблица не может быть пустой.")

    # Печатаем заголовки
    headers = table.keys()
    print("\t".join(headers))

    # Печатаем данные
    rows = zip(*table.values())
    for row in rows:
        print("\t".join(map(str, row)))
