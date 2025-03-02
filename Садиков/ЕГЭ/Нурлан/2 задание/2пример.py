def R(N):
    b = bin(N)[2:]
    if N % 5:
       tmp = b + bin(N % 5 * 5)[2:]
    else:
        tmp = b[:3] + b
    return int(tmp, 2)

for N in range(100, 10, -1):
    if N % 2 and R(N) < 313:
        print(N)
        break