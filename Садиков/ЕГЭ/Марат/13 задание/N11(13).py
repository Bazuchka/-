#Для узла с IP-адресом 214.32.112.131 адрес сети равен 214.32.64.0. 
#Чему равен третий слева байт маски? Ответ запишите в виде десятичного числа.
from ipaddress import *
for mask in range(33):
    net = ip_network('214.32.112.131/' + str(mask),0)
    if net.network_address == ip_address('214.32.64.0'):
        print(net.netmask)