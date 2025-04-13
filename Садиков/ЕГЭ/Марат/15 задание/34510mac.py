for A in range(32):
    B = 0
    for x in range(32):
        if ((x&25!=0) <= ((x & 9 == 0) <= (x&A!=0)))==0:
            B = 0
        else:
            B = B + 1    
    if B == 32:
        print(A)
        break