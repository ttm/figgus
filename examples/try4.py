import figgus as f

n=4
grains=[f.UnitGrain(),f.UnitGrain(),f.UnitGrain(),f.UnitGrain()]
s=f.Sequence(grains)

def doCompass(durs,freqs,perms,ncomps):
    for i in xrange(n):
	s.ordered_unit_grains[i].freq=eval(freqs)
	s.ordered_unit_grains[i].duration=eval(durs)
	print 1*(i+1)

    p=f.Pattern(s,f.PermutationPattern(),ncomps)
    p.synthesizeSonicVectors()
    return p.sonic_vector

semitom = "2**(1/12.)" # multiplication factor, 12 semintons gives an octave: 2 doubles de freqs
dur=".2"
sound=[]
sound+=2*doCompass(dur,"200*("+semitom+")**(3*i)",(2,3,1),3)
sound+=2*doCompass(dur,"200*("+semitom+")**(3*i)",(2,3,1),3)

sound2=doCompass(dur,".4*200*("+semitom+")**(3*i)",(2,3,1),1)
sound2+=doCompass(dur,"200*("+semitom+")**(3*i)",(2,3,1),1)
sound += 2*(3*sound2)

sound2=doCompass(dur,".4*200*("+semitom+")**(3*i)",(2,3,1),1)
sound2+=doCompass(dur,"100*("+semitom+")**(3*i)",(2,3,1),1)
sound += 2*(3*sound2)

sound*=2

io=f.IOUtils()
io.recordFile("som.wav",sound)