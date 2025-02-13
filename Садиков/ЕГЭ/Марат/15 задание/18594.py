for A in range(0, 300):
    k = 0
    for m in range(0, 30):
        for n in range(0, 30):
            if ((2 * m + 3 * n > 43) or (m < A) or (n <= A)) == 1:
                k += 1
    if k == 900:
        print(A)