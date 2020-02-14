import sys
import telnetlib
from socket import*

TCPIP = "10.224.0.130" # Endereco IP do dispositivo
PORT = 991            # Porta de comunicacao
# lista de dados requisitados
msg = [b"DAW0", b"DMW0", b"DMW1", b"DMW5"]

tcpSocket = socket(AF_INET, SOCK_STREAM)
tcpSocket.connect((TCPIP, PORT))

#tcpSocket.read_until(b"\r\n>")
for i in range(len(msg)):
    tcpSocket.send(msg[i] + b"\r")
    msg[i] = tcpSocket.recv(1024)
    

tcpSocket.close()
#tn.read_until(b"\r\n>")

print("Fim da transmissão!!!")
print("dado: ", msg)
#print ("PLC: ", NAMEPLC + "\n")
#print ("WORD MEMORY: ", Data + "\n")
#Data = str(tn.read_lazy())