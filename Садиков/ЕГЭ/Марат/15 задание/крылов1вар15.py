for A in range (1, 1000):
    k = 0
    for x in range (1, 1000):
        if (((x % 9 == 0) <= (not(x % 6 == 0))) or (x + A >= 100)):
            k += 1
        if k == 999:
            print(A)
            break


