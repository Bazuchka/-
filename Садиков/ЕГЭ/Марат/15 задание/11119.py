#На числовой прямой даны два отрезка: P  =  [20, 50] и Q  =  [30,65]. Отрезок A таков, что формула
#¬(x ∈ A) → ((x ∈ P) →¬ (x ∈ Q)) истинна при любом значении переменной x. Какова наименьшая возможная длина отрезка A?
#for P in range (20, 51):
#    for Q in range (30, 66):
#        for A in range (20, 50):
#            k = 0
#            for x in range (0, 100):
#                if ((not(x & A)) <= ((x % P) <= (not(x & Q)))) == True:
#                    k += 1
#            if k == 99:
#                print(A)
#                break

#Решение из Сайта
#Выражение ((x in P) <= (not(x in Q))) будет истинным, если:
#Если x содержится в P, то x не должен содержаться в Q.
# Требуется решить графический

m = 10**6
P = [i for i in range(20, 51)]                                  #Определяем границу P, цикл внутри списка, граница будет храниться в списке
Q = [i for i in range(30, 66)]                                  #Определяем границу P, цикл внутри списка, граница будет храниться в списке
for Amin in range(1, 100):                                      #Цикл для нахождения минимального значения А от 1 до 100
    for Amax in range(Amin + 1, 100):                           #Цикл для нахождения максимального значения А от 100 до 1 в обратном порядке
        check = 1
        A = [i for i in range(Amin, Amax)]                      #Цикл заполняет список А 
        for x in range(-100, 100):                              #Запускаем цикл для х
            f = (not(x in A)) <= ((x in P) <= (not(x in Q)))    #Переменная с выражением  not(x in A) — проверяет, не содержится ли x в списке A./x in P — проверяет, содержится ли x в списке P./not(x in Q) — проверяет, не содержится ли x в списке Q.
            if not f:                                           #Если f ложно
                check = 0                                       #То check = 0
                break                                           #Прервать цикл            
        if check == 1:                                          #Если чек не изменился то вычисляем m
            m = min(m,Amax - Amin)                              #На всем промежутке по А чек не должен менять значение
print(m-1)                                                      