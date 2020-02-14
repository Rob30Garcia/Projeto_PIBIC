import sys
import socket 

TCPIP = input("Digite o IP: ") #"192.168.100.5"
PORT = 991
a = b"MA1.0=1"
b = b"MA1.1=1"
c = b"MA1.2=1"
d = b"MA1.3=1"
e = b"MA1.4=0"

CMDRD = [a, b, c, d]
#CMDRD = [b"DMW0\r"]
 
addr = (TCPIP,PORT)

cmdSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cmdSocket.connect(addr)
#print(cmdSocket.getpeername())
#print(socket.gethostname())

for i in range(len(CMDRD)):
    cmdSocket.send(CMDRD[i] + b"\r")
    print(cmdSocket.recv(256))

cmdSocket.close()
print ("*** Fim da mensagem enviada ***") 