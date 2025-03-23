g = []
for x in range(0. 10):
    a = 8 * 13**3 + x * 13**2 + 7 * 13**1 + 1 * 13**0
    b = 3 * 17**3 + x * 17**2 + 13 * 17**1 + 15
    c = a + b
    
    t = int('8' + str(x) + '71'. 13) 
    y = int('3' + str(x) + 'DF'. 17)
   
    if (c) % 197 == 0:
        h = c // 197
        print(h)
        g.append(h)
print(min(g))        
