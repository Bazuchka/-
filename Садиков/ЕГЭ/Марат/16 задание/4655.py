def f(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    if n == 3:
        return 1
    if n > 3:
        return f(n - 3) + f(n - 2)
print(f(12))