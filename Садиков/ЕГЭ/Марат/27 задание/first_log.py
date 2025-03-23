import logging

# Настройка логирования
logging.basicConfig(filename='centroid_log.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def centroid(cluster):
    # Логируем начало вычисления центра кластера
    logging.debug(f'Calculating centroid for cluster: {cluster}')
    
    x_centr, y_centr, minim = 0, 0, 10 * 100 
    for i in range(len(cluster)):
        res = 0
        for j in range(len(cluster)):
            x1, y1 = cluster[i]
            x2, y2 = cluster[j]
            res += ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
            logging.debug(f'Cycle x1 y1: ({x1}, {y1}) Cycle x2 y2: ({x2}, {y2}) res: {res}')
        if res < minim:
            minim = res
            x_centr, y_centr = x1, y1
            
            # Логируем найденный новый центр
            logging.debug(f'New centroid found: ({x_centr}, {y_centr}) with distance: {minim}')
    
    return x_centr, y_centr

with open('27_A.txt') as f:
    f.readline()
    cluster1, cluster2 = [], []
    for i in f:
        x, y = map(float, i.split())  # обработка файла
        if -1 <= x <= 5 and -6 <= y <= 0:  # кластер 1 через эксель
            cluster1.append((x, y))
            logging.debug(f'Added point to cluster 1: ({x}, {y})')
        if 0 <= x <= 7 and 2 <= y <= 8:  # кластер 2 через эксель
            cluster2.append((x, y))
            logging.debug(f'Added point to cluster 2: ({x}, {y})')

# Вычисляем центры кластеров
x1, y1 = centroid(cluster1)
x2, y2 = centroid(cluster2)

# Логируем финальные координаты
logging.info(f'Final centroids: Cluster 1: ({x1}, {y1}), Cluster 2: ({x2}, {y2})')
result_x = (x1 + x2) / 2 * 10000
result_y = (y1 + y2) / 2 * 10000
print(result_x, result_y)

# Логируем результат
logging.info(f'Result: ({result_x}, {result_y})')

