f = open('24_5.txt')
s = f.readline()
k = 1
maxd = 0
'''for i in range(len(s) - 1):
    if s[i] != 'P' and s[i + 1] != 'P':
        k += 1
        maxd = max(maxd, k)
    else:
        k = 1
print(maxd)'''
for i in range(len(s) - 1):
    if s[i] == 'P' and s[i + 1] == 'P':
        k = 1
    else:
        k += 1
        maxd = max(maxd, k)
print(maxd)