f = open('24_4.txt')
s = f.readline()
k = 1
maxd = 0
for i in range(len(s) - 1):
    if s[i] in 'ABC' and s[i + 1] in '123':
        k += 1
        maxd = max(maxd, k)  
    elif s[i] in '123' and s[i + 1] in 'ABC':
        k += 1
        maxd = max(maxd, k)
    else:
        k = 1
print(maxd)