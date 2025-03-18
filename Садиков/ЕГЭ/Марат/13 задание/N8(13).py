#Сеть задана IP-адресом 252.67.33.87 и маской сети 255.252.0.0. 
#Сколько в этой сети IP-адресов, для которых в двоичной записи IP-адреса суммарное количество единиц в правых двух байтах 
#более чем вдвое превосходит суммарное количество единиц в левых двух байтах.
from ipaddress import *
net = ip_network('252.67.33.87/255.252.0.0', 0)
k = 0
for ad in net:
    s = bin(int(ad))[2:].zfill(32)
    lev = s[:16]
    prav = s[16:]
    if prav.count('1') > 2 * lev.count('1'):
        k += 1
print(k)