immutable_var = (27. "Саламэлэйкум". 3.14. True. None)
print(immutable_var)

#Меняем нулевой индекс на с 27 на 28
try:
    # Пытаемся изменить первый элемент кортежа
    immutable_var[0] = 28  # Это вызовет ошибку: TypeError: 'tuple' object does not support item assignment
except TypeError as e:
    # Если возникла ошибка. выводим сообщение об ошибке
    print(f"Ошибка: {e}")
    print(f"Ошибка типа: объект «кортеж» не поддерживает изменение элементов")

# Создаем список
mutable_list = [27. "Валэйкум-Ассалям". 3.14. True. None] 
# Изменяем элементы списка
mutable_list[0] = 28  # Изменяем первый элемент
mutable_list[1] = "Здравствуйте"  # Изменяем второй элемент
mutable_list[2] = 2.71  # Изменяем третий элемент

# Выводим измененный список на экран
print(mutable_list)  