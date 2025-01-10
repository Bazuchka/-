#Значение выражения 1255 + 259 − 30? записали в системе счисления с основанием 5.
#Сколько цифр 4 содержится в этой записи?

def f(n):                               #объявили функцию
    s = ''                              #пустая переменная тип строка
    while n > 0:                        # пока переменная больше 0
        s = str(n % 5) + s              #возвращает остаток от деления 
        n = n // 5                      #целочисленное деление
    return s                            #конец функции вернуть значение 
a = f(125**5 + 25**9 - 30).count('4')   #пример
print (a)

 