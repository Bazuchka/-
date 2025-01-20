# Начало
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
# Сортировка студентов
students_sort = sorted(list(students))
print(students_sort)#Проверка
# Словарь
average_grades = dict(zip(students_sort, map(lambda g: sum(g) / len(g), grades)))
print(average_grades)
#функция map, которая применяет функцию к каждому элементу из grades.
#внутри лямбда анонимная функция, которая принимает список оценок g, суммирует их с помощью sum(g) и делит на количество оценок len(g), чтобы получить среднее значение.