#Напишите наибольшее целое число, для которого истинно высказывание:
#НЕ(Число > 10 000) И (Число нечетное).

for x in range(0,2000):
    if not(x > 10000) and x % 2 != 0:
        print(x)
