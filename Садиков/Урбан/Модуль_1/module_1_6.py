#Пункт 2
print("\nПункт2")
# Создаем словарь с несколькими парами ключ-значение
my_dict = {"Имя": "Ильнур","Год рождения": 1997}

# Выводим словарь на экран
print("Словарь my_dict:", my_dict)

# Выводим значение по существующему ключу
print("Имя:", my_dict["Имя"])

# Попробуем вывести значение по отсутствующему ключу без ошибки
# Используем метод get, который возвращает None, если ключ отсутствует
print("Возраст:", my_dict.get("Возраст", "Ключ не найден"))

# Добавляем еще две произвольные пары в словарь
my_dict["Город"] = "Набережные Челны"
my_dict["Профессия"] = "Системный аналитик"

# Удаляем одну из пар по существующему ключу и выводим значение на экран
removed_value = my_dict.pop("Год рождения", "Ключ не найден")
print("Удаленное значение:", removed_value)

# Выводим обновленный словарь на экран
print("Обновленный словарь:", my_dict)

#Пункт 3
print("\nПункт3")
# Создаем множество с разными типами данных и повторяющимися значениями
my_set = {1, "Привет", 3.14, True, 1, "Привет"}

# Выводим множество на экран (должны отобразиться только уникальные значения)
print("Исходное множество:", my_set)

# Добавляем 2 произвольных элемента в множество, которых еще нет
my_set.add("Челны")
my_set.add(28)

# Удаляем один любой элемент из множества
my_set.remove("Челны")  

# Выводим измененное множество на экран
print("Измененное множество:", my_set)