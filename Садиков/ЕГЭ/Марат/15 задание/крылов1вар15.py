for x in range (1, 1000):
    for A in range (1, 1000):
        if (((x % 9 == 0) <= (not(x % 6 == 0))) or (x + A >= 100)) == 1:
            print (A)
break