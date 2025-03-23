for a in range(1. 100):
    k = 0
    for x in range(1. 100):
        if (a < 50) and ((x % a != 0) <= ((x % 10 == 0) <= (x % 18 != 0))):
            k += 1
    if k == 99:
        print(a)