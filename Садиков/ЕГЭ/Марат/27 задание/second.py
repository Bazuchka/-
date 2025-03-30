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
with open('demo_2025_27_А.txt') as f:
    f.readline()
    cluster1, cluster2 = [], []
    for i in f:
        x,y = map(float, i.replace(',', '.').split())#обработка файла
        if -2 <= x <= 1 and -1 <= y <= 3:# кластер 1  через эксель
            cluster1.append((x,y))
        if 1 <= x <= 5 and 3 <= y <= 7:# кластер 2 через эксель
            cluster2.append((x,y)) 
             
x1, y1 = centr(cluster1)
x2, y2 = centr(cluster2)

print((x1 + x2) / 2 * 10000, (y1 + y2) / 2 * 10000)
