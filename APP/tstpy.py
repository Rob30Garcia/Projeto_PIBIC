import sys
import telnetlib

TCPIP = "10.224.0.130"
PORT = "991"
CMDRD = [b"MA1.0=0", b"MA1.1=0", b"MA1.2=0", b"MA1.3=0"]
#CMDRD = b"MA0.4=1"
#tam = len(CMDRD) - 1

tn = telnetlib.Telnet()
tn.open(TCPIP, PORT)
#tn = telnetlib.Telnet(open(TCPIP), PORT)
#tn.read_until(">",  timeout=None)
#print (tn.interact())

#tn.write(b"MM0.0=1" + b"\r\n")
#tn.write(b"MM5.0=1" + b"\r\n")
for i in range(len(CMDRD)):
    tn.write(CMDRD[i] + b"\r\n")

tn.write(b"")

Data = tn.write(b"DMW0" + b"\r\n")

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