from FIGGUS import *
import pylab as P

p=Pattern()
p.synthesizeSonicVectors()
#print p.sonic_vector #eh pra rolar 3s de senoide a 220Hz, (sao 3 x 1s)

io=IOUtils()
io.recordPattern("som.wav",p)
