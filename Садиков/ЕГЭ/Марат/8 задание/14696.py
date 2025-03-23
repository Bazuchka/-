k = 0
alf = 'АПРСУ'
for x1 in alf:
    for x2 in alf:
        for x3 in alf:
            k += 1
            s = x1 + x2 + x3
            if s[0] == 'С':
                print(k)
                break