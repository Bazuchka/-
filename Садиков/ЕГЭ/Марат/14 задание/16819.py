#Значение выражения 1255 + 259 − 30? записали в системе счисления с основанием 5.
#Сколько цифр 4 содержится в этой записи?
def f(n):
    s = ''
    while n > 0:
        s = str(n % 5) + s
        n = n // 5
    return s
a = f(125**5 + 25**9 - 30).count('4')
print (a)

 