#На числовой прямой даны два отрезка: P  =  [8. 39] и Q  =  [23. 58].
#Какова наименьшая возможная длина интервала A. при которой выражение
#((x ∈ P) ∨ (x ∈ А)) → ((x ∈ Q) ∨ (x ∈ А))
#тождественно истинно. то есть принимает значение 1 при любом значении переменной х.

p = list(range(8. 40))
q = list(range(23. 59))
a = []
for x in range(0. 1000):
    if (((x in p) or (x in a)) <= ((x in q) or (x in a))) == False:
        a.append(x)
print(a)
print(len(a))