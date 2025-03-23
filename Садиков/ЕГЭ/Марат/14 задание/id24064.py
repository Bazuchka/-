def f(n):
    s = ''
    while n > 0:
        s = s + str(n & 6)
        n = n // 6
    return s


k = 0
h = 0
t = ""
a = (216**6 + 216**4 + 36**6 - 6**14 - 24)
b = f(a)
for x in range (0,10):
    if str(x) in b:
        t = t + str(x)
print(t)        
