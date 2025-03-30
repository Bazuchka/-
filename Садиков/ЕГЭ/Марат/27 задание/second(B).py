def centr(cluster):
    x_centr, y_centr, minim = 0, 0, 10**10
    for i in range(len(cluster)):
        res = 0
        for j in range(len(cluster)):
            
            x1, y1 = cluster[i]
            x2, y2 = cluster[j]
            res += ((x2- x1)**2 + (y2 - y1)**2) ** 0.5
        if res < minim:
            minim = res
            x_centr, y_centr = x1, y1
    return x_centr, y_centr

with open('demo_2025_27_Б.txt') as f:
    f.readline()
    cluster1, cluster2, cluster3 = [], [], []
    for i in f:
        x,y = map(float, i.replace(',', '.').split())#обработка файла
        if 0 <= x <= 3 and 0 <= y <= 4:# кластер 1  через эксель
            cluster1.append((x,y))
        if 2 <= x <= 5 and 6 <= y <= 12:# кластер 2 через эксель
            cluster2.append((x,y)) 
        if 5 <= x <= 8 and 4 <= y <= 8:
            cluster3.append((x,y))
             
x1, y1 = centr(cluster1)
x2, y2 = centr(cluster2)
x3, y3 = centr(cluster3)

print(x1, y1)
print((x1 + x2 + x3) / 3 * 10000, (y1 + y2 + y3) / 3 * 10000)
