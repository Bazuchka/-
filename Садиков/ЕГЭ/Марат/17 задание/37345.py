f = open('17.txt')
a = []
for s in f:
    a.append(int(s))
print(len(a))    
k = 0
maxs = -10**10
for i in range(len(a)-1):
    if i == 9998:
        b = a[i+1]
        print(b)
    for j in range(i + 1, len(a)):
        if (a[i] * a[j]) % 62 == 0:
            k += 1
            maxs = max(maxs, a[i] + a[j])
print(k, maxs)