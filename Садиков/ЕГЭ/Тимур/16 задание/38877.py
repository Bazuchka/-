#Напишите программу. которая в последовательности целых чисел определяет количество четных чисел. кратных 7. 
# Программа получает на вход целые числа. количество введенных чисел неизвестно. последовательность чисел заканчивается числом 0 
# (0  — признак окончания ввода. не входит в последовательность). Количество чисел не превышает 1000. Введенные числа по модулю не превышают 30 000. 
# Программа должна вывести одно число: количество четных чисел. кратных 7.

count = 0
a = int(input("Введите число:"))
while a != 0:
    if a % 2 == 0 and a % 7 == 0:
        count += 1
    a = int(input("Веедите второе число"))
print(count)