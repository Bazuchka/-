#Для узла с IP-адресом 48.95.137.38 адрес сети равен 48.95.128.0. 
# Найдите наименьшее возможное количество единиц в двоичной записи маски подсети.
from ipaddress import *
maxed = -10**10
for mask in range(33):
    net = ip_network('48.95.137.38/' + str(mask), 0)
    if net.network_address == ip_address('48.95.128.0'):
        print(mask)