#Введем данные и конвертируем их. т.к. input возвращает string
first  = int(input('Введите первое число'))
second = int(input('Введите второе число'))
third  = int(input('Введите третье число'))

if first == second and first == third and third == second:
    print("3")
elif first == second or first == third or third == second:   
    print("2")
else: 
    print("0")