import figgus as f

n=4
grains=[f.UnitGrain(),f.UnitGrain(),f.UnitGrain(),f.UnitGrain()]
s=f.Sequence(grains)

def doCompass(durs,freqs,perms,ncomps):
    for i in xrange(n):
	s.ordered_unit_grains[i].freq=eval(freqs)
	s.ordered_unit_grains[i].duration=eval(durs)
	#print 1*(i+1)

    p=f.Pattern(s,f.PermutationPattern(perms),ncomps)
    p.synthesizeSonicVectors()
    return p.sonic_vector

semitom = "2**(1/12.)" # multiplication factor, 12 semintons gives an octave: 2 doubles de freqs
dur=".2"
sound=[]

######
sound1=doCompass(dur,"200*("+semitom+")**(3*i)",(2,3,1),3)
sound1B=doCompass(dur,"4*200*("+semitom+")**(3*i)",(2,3,1),3)
sound1C=doCompass(dur,".5*200*("+semitom+")**(3*i)",(2,3,1),3)
sound2=doCompass(dur,"200*("+semitom+")**(3*i)",(3,1,2),3) # Inverting quirality
sound2B=doCompass(dur,"4*200*("+semitom+")**(3*i)",(3,1,2),3) # Inverting quirality
sound2C=doCompass(dur,".5*200*("+semitom+")**(3*i)",(3,1,2),3) # Inverting quirality
silencio=doCompass(dur,"0",(2,3,1),1)

sound+=[(i+j)*.5 for i,j in zip(sound1,sound1C)]
sound+=[(i+j)*.5 for i,j in zip(sound2B,sound2C)]


sound += 2*[(i+j)*.5 for i,j in zip(sound1,sound2B)]
sound += 2*[(i+j)*.5 for i,j in zip(sound1B,sound2)]

sound+=[(i+j+k)*.32 for i,j,k in zip(sound1,sound1C,sound2B)]
sound+=[(i+j+k)*.32 for i,j,k in zip(sound2B,sound2C,sound2B)]

sound += [(i*j)*.32 for i,j,k in zip(sound1B,sound2,sound2C)]
sound += [(i*j)*.32 for i,j,k in zip(sound1,sound2B,sound2C)]



######

sound += (2*sound)

io=f.IOUtils()
io.recordFile(sound)