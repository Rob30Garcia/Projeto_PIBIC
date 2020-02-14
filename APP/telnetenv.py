import sys
import telnetlib

# Metodo usando telnetlib para enviar 
# mensagem de comando para o dispositivo

TCPIP = "10.224.0.130"
PORT = str(991) 
CMDRD = [b"MM1.0=1", b"MM1.1=1", b"MM1.2=1", b"MM1.3=1"]
#CMDRD = [b"DMW0"]

tn = telnetlib.Telnet(TCPIP, PORT, timeout=5)
#tn.set_debuglevel(2000)

tn.read_until(b"\r\n>")
for i in range(len(CMDRD)):
    tn.write(CMDRD[i] + b"\r\n")

tn.close()
print("*** Fim da mensagem enviada ***")