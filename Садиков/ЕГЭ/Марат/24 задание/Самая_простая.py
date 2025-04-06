# все работает
f=open('24_1.txt')
s=f.read()
k=0
kmax=0

for i in range(0, len(s)):
    if s[i]=='B':
        k=k+1
        kmax=max(k, kmax)
    else:
        k=0

print(kmax)