def f(n):
    s = ''
    while n > 0:
        s = str(n % 16) + s
        n = n // 16
    return s
a = 3 * 4**38 + 2 * 4**23 + 4**20 + 3 * 4**5 + 2 * 4**4 + 1
b = f(a)
if b[0] != 0:
    c = b.count('0') 
print(c. b)