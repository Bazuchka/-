for A in range (1. 1000):
    count = 0
    for x in range (1. 1000):
        if (((x % 9 == 0) <= (not(x % 6 == 0))) or (x + A >= 100)) == 1:
            count = count + 1
    if count == 999:
        print ("Answer = ".count.A)
        break
                
   
