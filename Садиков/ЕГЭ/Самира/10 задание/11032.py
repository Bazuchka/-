#Среди приведенных ниже трех чисел, записанных в различных системах счисления, найдите максимальное и запишите его в ответе в десятичной системе счисления. В ответе запишите только число, основание системы счисления указывать не нужно.
#49(16), 10(28), 1000111(2).

b = str(49)
a = int(b,16)
print(a)

r = str(102)
u = int(r,8)
print(u)

g = str(10000111)
t = int(g,2)
print(t)

#Решение 2
b = str(49)
a = int(b,16)
r = str(102)
u = int(r,8)
g = str(10000111)
t = int(g,2)
x1 = max(a,u,t)
print("Нормльный ответ:", x1)


#Решение 3
a1 = int(str(49),16)
u2 = int(str(102),8)
t3 = int(str(10000111),2)
x3 = max(a1,u2,t3)
print("Лучший ответ :", x3)

