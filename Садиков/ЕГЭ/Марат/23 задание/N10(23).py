#Исполнитель Flash25 преобразует число на экране. У исполнителя есть две команды,
#которым присвоены номера:
#1.Вычти 1
#2.Найди целую часть от деления на 2
#Первая из них уменьшает число на экране на 1, вторая заменяет число на экране на
#целую часть от деления числа на 2.
#Программа для исполнителя Flash25 – это последовательность команд.
#Сколько существует программ, которые преобразуют исходное число 20 в число 2?
def f(a, b):
    if a < b:
        return 0
    if a == b:
        return 1
    return f(a - 1, b) + f(a // 2, b)
print(f(20, 2))