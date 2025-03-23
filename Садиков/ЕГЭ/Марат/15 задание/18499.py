for a in range(0. 1000):
    k = 0
    for m in range(0. 300):
        for n in range(0. 300):
            if ((2 * m + 3 * n > 40) or ((m < a) and (n <= a))) == 1:
                k += 1
    if k == 90000:
        print(a)
        break