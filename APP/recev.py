import sys
import socket 

TCPIP = "10.224.0.130" # "192.168.100.5"
PORT = 991
CMDRD = [b"DAW0", b"DMW0", b"DMW1", b"DMW5"]

addr = (TCPIP,PORT)

rcvSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
rcvSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
rcvSocket.bind(addr)
rcvSocket.listen(10)

conn, cliente = rcvSocket.accept() 
print ("*** Conectado ***")
for i in range(len(CMDRD)):
    rcvSocket.send(CMDRD[i] + b"\r")
    print(rcvSocket.recv(256))

cmdSocket.close()
print(type(data))
print ("*** Fim da mensagem recebida ***") 