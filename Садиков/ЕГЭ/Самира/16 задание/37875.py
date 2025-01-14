s = 0
a = int(input("Введите число а = "))
while a != 0:
    if (a % 7 == 0) and (a % 10 == 3):
        s = s + a
    a = int(input("Введите число а1 = "))
print(s)