#Урок 1: Практическая работа по уроку "Динамическая типизация"
#Автор: Садиков Ильнур Айдарович
#Дата 23.12.2024

Name = "John" #Имя тип данных string
Age = 25 #возраст
New_Age = Age + 1 # новый возраст = 25 + 1
Is_Student = True #присвоил переменной true  
print("Имя:", Name, "\nВозраст: ", Age, "\nВозраст+1: ", New_Age, "\nЯвляется ли студентом: ",  Is_Student)

#Усложним добавим инпут и с помощью возраста определим является ли студентом
print("\nУсложненный вариант для того, чтобы переменная Is_Student стал логичным")

age_input = int(input('Введите ваш возраст: '))
if age_input < 26 and age_input > 16:
    Is_Student = True
else:
    Is_Student = False
if Is_Student == True:
    AgePR = 'Да'
else:    
    AgePR = 'Нет'
print("Имя:", Name, "\nВозраст: ", age_input, "\nЯвляется ли студентом: ",  AgePR)

