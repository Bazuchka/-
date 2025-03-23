def centroid(cluster): # ищем центр кластера
    x_centr, y_centr, minim = 0, 0, 10 * 100 
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

with open('27_A.txt') as f:
    f.readline()
    cluster1, cluster2 = [], []
    for i in f:
        x,y = map(float, i.split())#обработка файла
        if -1 <= x <=5 and -6 <= y <= 0:# кластер 1  через эксель
            cluster1.append((x,y))
        if 0 <= x <= 7 and 2 <= y <= 8:# кластер 2 через эксель
            cluster2.append((x,y)) 
             
x1, y1 = centroid(cluster1)
x2, y2 = centroid(cluster2)

print((x1 + x2) / 2 * 10000, (y1 + y2) / 2 * 10000)

