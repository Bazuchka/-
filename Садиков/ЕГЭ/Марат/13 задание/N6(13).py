#(ЕГЭ 2024 день 2) В терминологии сетей TCP/IP маской сети называют двоичное число. которое показывает. 
#какая часть IP-адреса узла сети относится к адресу сети. а какая – к адресу узла в этой сети. 
#Адрес сети получается в результате применения поразрядной конъюнкции к заданному адресу узла и маске сети.
#Сеть задана IP-адресом 112.160.0.0 и маской сети 255.240.0.0
#Сколько в этой сети IP-адресов. для которых количество единиц в двоичной записи IP-адреса кратно 5? В ответе укажите только число.
from ipaddress import *
net = ip_network('112.160.0.0/255.240.0.0'. 0)
k = 0
for ad in net:
    if bin(int(ad))[2:].zfill(32).count('1') % 5 == 0:
        k += 1
print(k)