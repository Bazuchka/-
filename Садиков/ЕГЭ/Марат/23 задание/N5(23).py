#Исполнитель Flash25 преобразует число на экране. У исполнителя есть три команды,
#которым присвоены номера:
#1. Прибавить 1
#2. Прибавить 2
#3. Прибавить 3
#Программа для исполнителя Flash25 – это последовательность команд.
#Сколько существует программ, для которых при исходном числе 3 результатом
#является число 15 и при этом траектория вычислений не содержит число 8? 
def f(a, b):
    if a > b or a == 8:
        return 0
    if a == b:
        return 1
    return f(a + 1, b) + f(a + 2, b) + f(a + 3, b)
print(f(3, 15))