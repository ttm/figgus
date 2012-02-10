from figgus import *

p=Pattern()
p.synthesizeSonicVectors()

io=IOUtils()
io.recordPattern("som.wav",p)
