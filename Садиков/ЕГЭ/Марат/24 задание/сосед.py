#Коды символов: Каждый символ имеет свой код в таблице Unicode. Например:

#'A' имеет код 65
#'B' имеет код 66
#Сравнение символов: Когда Вы сравниваете два символа, Python фактически сравнивает их коды.

f=open('сосед.txt')
s=f.read().rstrip()
k=1
kmax=0

for i in range(0, len(s)-1):
    if s[i]<=s[i+1]:
        k=k+1
        kmax=max(k, kmax)
    else:
        k=1

print(kmax)