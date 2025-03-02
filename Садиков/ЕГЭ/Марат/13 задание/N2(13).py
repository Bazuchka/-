#Если маска подсети 255.255.224.0 и IP-адрес компьютера в сети 206.158.124.67, 
# то номер компьютера в сети равен_____
from ipaddress import *
net = ip_network('206.158.124.67/255.255.224.0', 0)
k = -1 #счет ip адрессов начинается с 0
for ad in net:
    k += 1
    if ad == ip_address('206.158.124.67'):
        print(k)
        break

#Подключаем библиотеку:
#from ipaddress import *
#Функция для создания объекта сети:
#net = ip_network('адрес сети/маска')
#Получить количесвто адресов:
#net.num_addresses
#Получение маски сети:
#net.netmask
#Цикл для перебора значений маски:
#for mask in range(33):
#net = ip_network('адрес узла/' + (mask), 0)
#Цикл для перебора IP-адресов в сети:
#for ip in net:
#Представление IP-адреса в двоичном виде:
#bin(int(ad))[2:].zfill(32)