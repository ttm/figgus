import figgus as f
n=4
grains=[f.UnitGrain(),f.UnitGrain(),f.UnitGrain(),f.UnitGrain()]
s=f.Sequence(grains)
for i in xrange(n):
    s.ordered_unit_grains[i].freq=10000 - 1000*(i+1)
    s.ordered_unit_grains[i].duration=.2 + 0.05*i
    #print 100*(i+1)
    
s.ordered_unit_grains[1].freq=100
s.ordered_unit_grains[3].freq=500
    
#pp=PermutationPattern()
p=f.Pattern(s,f.PermutationPattern(),42)
p.synthesizeSonicVectors()

io=f.IOUtils()
io.recordPattern("som.wav",p)

#print "== Ouca que 'o triangulo gira e existe uma bola do lado' (nome da peca) =="