#У исполнителя Flash25 две команды, которым присвоены номера:
#1. прибавь 2
#2. умножь на 2
#Сколько есть программ, которые число 1 преобразуют в число 10?
def f(a, b):
    if a > b:
        return 0
    if a == b:
        return 1
    return f(a + 2, b) + f(a * 2, b)
print(f(1, 10))