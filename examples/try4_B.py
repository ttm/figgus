import figgus as f

n=4
grains=[f.UnitGrain(),f.UnitGrain(),f.UnitGrain(),f.UnitGrain()]
s=f.Sequence(grains)

def doCompass(durs,freqs,perms,ncomps):
    for i in range(n):
    	s.ordered_units[i].freq=eval(freqs)
    	s.ordered_units[i].duration=eval(durs)

    p=f.Pattern(s,f.PermutationPattern(perms),ncomps)
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

# Inverting quirality
sound+=2*doCompass(dur,"200*("+semitom+")**(3*i)",(3,1,2),3)
sound+=2*doCompass(dur,"200*("+semitom+")**(3*i)",(3,1,2),3)

sound2=doCompass(dur,".4*200*("+semitom+")**(3*i)",(3,1,2),1)
sound2+=doCompass(dur,"200*("+semitom+")**(3*i)",(3,1,2),1)
sound += 2*(3*sound2)

sound2=doCompass(dur,".4*200*("+semitom+")**(3*i)",(3,1,2),1)
sound2+=doCompass(dur,"100*("+semitom+")**(3*i)",(3,1,2),1)
sound += 2*(3*sound2)

io=f.IOUtils()
io.recordFile(sound)# records to 'sound.wav'
