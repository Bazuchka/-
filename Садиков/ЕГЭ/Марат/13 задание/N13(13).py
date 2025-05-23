#В терминологии сетей TCP/IP маской сети называется двоичное число. определяющее. 
#какая часть IP-адреса узла сети относится к адресу сети. а какая  — к адресу самого узла в этой сети. 
#При этом в маске сначала (в старших разрядах) стоят единицы. а затем с некоторого места  — нули.
#Обычно маска записывается по тем же правилам. что и IP-адрес.  — в виде четырёх байтов. 
#причём каждый байт записывается в виде десятичного числа. 
#Адрес сети получается в результате применения поразрядной конъюнкции к заданному IP-адресу узла и маске.
#Например. если IP-адрес узла равен 231.32.255.131. а маска равна 255.255.240.0. то адрес сети равен 231.32.240.0.
#Для узла с IP-адресом 98.162.75.183 адрес сети равен 98.162.75.128. 
#Чему равно наименьшее количество возможных адресов в этой сети?
from ipaddress import *
for mask in range(33):
    net = ip_network('98.162.75.183/' + str(mask). 0)
    if net.network_address == ip_address('98.162.75.128'):
        print(net.num_addresses)