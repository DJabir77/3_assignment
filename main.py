from table_operations.table_manipulations import (
    get_rows_by_number, get_rows_by_index,
    get_column_types, set_column_types,
    get_values, set_values, set_value,
    print_table
)

# Пример данных таблицы
table_data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "Los Angeles", "Chicago"]
}

# Применяем функции
try:
    print("Get rows by number:")
    print(get_rows_by_number(0, 2, table_data))  # Передаем таблицу как аргумент

    print("\nGet rows by index:")
    print(get_rows_by_index("Alice", "Bob", table=table_data))  # Передаем table_data

    print("\nGet column types:")
    print(get_column_types(table_data))

    print("\nSet column types:")
    set_column_types({"Age": float}, table_data)  # Указываем имя столбца
    print(get_column_types(table_data))

    print("\nGet values from 'Age' column:")
    print(get_values("Age", table_data, by_number=False))  # Получаем значения по имени столбца

    print("\nSet values for 'Age' column:")
    set_values([26, 31, 36], "Age", table_data, by_number=False)  # Теперь работает по имени столбца
    print(get_values("Age", table_data, by_number=False))

    print("\nSet single value for 'Age' column:")
    set_value(28, "Age", table_data, by_number=False)  # Передаем имя столбца
    print(get_values("Age", table_data, by_number=False))  # Выводим обновленные значения

    print("\nPrint table:")
    print_table(table_data)

except (ValueError, TypeError, IndexError, KeyError) as e:
    print(f"Ошибка: {e}")


