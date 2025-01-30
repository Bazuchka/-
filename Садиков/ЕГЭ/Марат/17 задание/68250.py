a = [int(s) for s in open('170.txt')]
a538 = max([x for x in a if x % 1000 == 538])
s4 = []
for i in range (len(a) - 3):
    cetverka = [a[i] , a[i+1] , a[i+2], a[i+3]]
    a5 = [x for x in cetverka if len(str(x)) >= 5]
    anot5 = [x for x in cetverka if len(str(x)) != 5]
    a3 = [x for x in cetverka if x % 3 == 0]
    a7 = [x for x in cetverka if x % 7 == 0]
    if len(a5) >= 2 and len(anot5) >= 1:
        if len(a3) > len(a7):
            if sum(cetverka) > a538 and sum(cetverka) < a538*2:
                s4.append(sum(cetverka))
print(len(s4),max(s4))       