f = open('24_3.txt')
s = f.readline()
k = 1
maxd = 0
for i in range(len(s) - 1):
    if s[i] != s[i + 1]:
        k += 1
        maxd = max(maxd, k)
    else:
        k = 1
print(maxd)