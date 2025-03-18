#(ЕГЭ 2024 день 2) В терминологии сетей TCP/IP маской сети называют двоичное число, 
#которое показывает, какая часть IP-адреса узла сети относится к адресу сети, а какая — к адресу узла в этой сети. 
#Адрес сети получается в результате применения поразрядной конъюнкции к заданному адресу узла и его маске.
#Сеть задана IP-адресом 157.180.63.114 и сетевой маской 255.255.255.248.
#Сколько в этой сети IP-адресов, для которых количество единиц в двоичной записи IP - адреса НЕ кратно 4? 
#В ответе укажите только число.
from ipaddress import *
net = ip_network('157.180.63.114/255.255.255.248', 0)
k = 0
for ad in net:
    if bin(int(ad)).zfill(32).count('1') % 4 != 0:
        k += 1
print(k)