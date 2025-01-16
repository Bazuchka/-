import sys
sys.float_info.max
1.7976931348623157e+308
sys.setrecursionlimit(10**6)
def f(n):
    if n == 1:
        return 1
    if n > 1:
        return n * f(n - 1)
print (((f(2025)/25) + f(2024))/f(2023))