#Исполнитель Flash25 преобразует целое число, записанное на экране. 
#У исполнителя две команды, каждой команде присвоен номер:
#1. Прибавь 1
#2. Умножь на 2
#Первая команда увеличивает число на экране на 1, вторая увеличивает это число в 2 раза. 
#Программа для исполнителя Flash25 – это последовательность команд.
#Сколько существует программ, которые число 5 преобразуют в число 32 и в которых предпоследняя команда 1?
def f(a, b):
    if a > b:
        return 0
    if a == b:
        return 1
    return f(a + 1, b) + f(a * 2, b)
print(f(5, 16) + f(5, 30))