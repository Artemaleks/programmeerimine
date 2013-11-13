import math
# -*- coding: utf-8 -*-

# taisnurkne kolmnurk
print " "
print "YLESANNE 1. Antud taisnurkne kolmnurk, mille hypotenuus c = 10 cm ja < alpha = 30°. Leiame selle kaatetid."  
print " "

c = 10.0 
alpha = 30

sin30 = math.sin(30/180.*math.pi)
print"sin30° = {}".format(sin30)

sin60 = math.sin(60/180.*math.pi)
print"sin60° = {}".format(sin60)

a = c * sin30
print"a (cm) = {}".format(a)

beta = 90 - alpha
print"beta (°) = {}".format(beta)

b = c * sin60
print"b (cm) = {}".format(b)

print "Vastus: a = 5 cm ja b ~ 8,7 cm."  






# v6rdhaarne kolmnurk
print " "
print "YLESANNE 2. Antud v6rdhaarne kolmnurk, mille kõrgus H = 15 cm, nurk haare ja aluse vahel = 45°. Leiame pindala."  
print " "

H = 15.00
alpha = 30

tanalpha = math.tan(30/180.*math.pi)
print"tanalpha = {}".format(tanalpha)

a = tanalpha * H
print"a (cm) = {}".format(a)

c = c = math.sqrt(a**2 + H**2)
print"c = {}".format(c)

pindala = (a * H)/2
print"pindala (cm**2) = {}".format(pindala)
print "Vastus: pindala ~ 65 cm**2."  












A
A
A
A
A
A
A

