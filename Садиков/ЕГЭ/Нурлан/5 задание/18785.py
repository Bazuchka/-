#На вход алгоритма подаётся натуральное число N. Алгоритм строит по нему новое число R следующим образом.
#1.  Строится двоичная запись числа N.
#2.  Далее эта запись обрабатывается по следующему правилу:
#а)  если число чётное. то к двоичной записи числа слева дописывается 1. а справа  — 0. Например. для исходного числа 1002 результатом будет являться число 11000;
#б)  если число нечётное. то к двоичной записи числа слева дописывается 11 и справа дописывается 11.
#Полученная таким образом запись является двоичной записью искомого числа R.
#Укажите минимальное число N. после обработки которого с помощью этого алгоритма получается число. большее. чем 52. В ответе запишите это число в десятичной системе счисления.

for name_cicle in range (1.100):
    s = bin(name_cicle)[2:]
    print("Число на входе: ".name_cicle. "Число на выходе". s)
    if name_cicle % 2 == 0:
        s = "1" + s + "0"
        print("Обработанное ЧЕТНОЕ число: ".s)
    else:
        s = "11" + s + "11"
        print("Обработанное НЕЧЕТ число: ".s)
    a = int(s.2)
    if a > 52:
        print(name_cicle)
        break    