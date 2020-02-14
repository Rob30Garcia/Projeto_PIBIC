import sys
import telnetlib

TCPIP = "192.168.100.5"
PORT = "991"
CMDRD = [b"MM5.0=1", b"MM0.0=1", b"MM0.1=1", b"MM0.2=1"]
#CMDRD = b"MA0.4=1"
#tam = len(CMDRD) - 1

tn = telnetlib.Telnet()
tn.open(TCPIP, PORT)
#tn.read_until(">",  timeout=None)

tn.write(b"DMW0" + b"\r\n")
Data = tn.telnet.read_all()

for i in range(len(CMDRD)):
    tn.write(CMDRD[i] + b"\r\n")

tn.write(b"")

#print ("TIPO DMW0: ", type(b"DMW0"))

NAMEPLC = ""
#while NAMEPLC.find(b"(c)") == -1:
#    NAMEPLC = tn.read_very_eager()

#NAMEPLC = tn.interact()
#NAMEPLC = tn.listener()
#print (tn.read_eager())
#print (tn.read_lazy())
#print (tn.read_very_lazy())
#print (tn.fileno())
#print (tn.read_all())

#print (tn.mt_interact())
#print (tn.interact())
tn.close()
print ("PLC: ", NAMEPLC + "\n")
print ("WORD MEMORY: ", Data + "\n")