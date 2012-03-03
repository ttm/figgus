import figgus as f

n=4
grains=[f.UnitGrain(),f.UnitGrain(),f.UnitGrain(),f.UnitGrain()]
s=f.Sequence(grains)

###########
# Construction loop: in each compass,
# I choose some parameters for our sequence,
# More sppeciffically, i choose parameters for
# each of the 4 units/grains and a permutation

# The permutation gives periodicity, inteligibility,
# and builds third order archs in the musical discourse
# 1st order: grain
# 2nd order: sequence/compass
# 3rd order: permutation cycle
# 4th order: permutation cycleS periods toguether and other aesthetic resources
# 5th order: the piece as it is
# 6th order: sets of pieces
# 7th order: the whole social/human context of the piece, life of the author, etc.
###
sound=[]

# COMPASS 1-4 *.*.*.*.*.*.*.*.*.*.*.*.* 1
def doCompass(durs,freqs,perms,ncomps):
    for i in xrange(n):
	s.ordered_unit_grains[i].freq=eval(freqs)
	s.ordered_unit_grains[i].duration=eval(durs)
	#print 1*(i+1)
	
    #s.ordered_unit_grains[1].freq=100
    #s.ordered_unit_grains[3].freq=500
	
    #pp=PermutationPattern()
    p=f.Pattern(s,f.PermutationPattern(),ncomps)
    p.synthesizeSonicVectors()
    return p.sonic_vector

#sound+=doCompass(".2 + 0.05*i","10000 - 1000*(i+1)")
semitom = "2**(1/12.)" # multiplication factor, 12 semintons gives an octave: 2 doubles de freqs
sound+=2*doCompass(".5","200*("+semitom+")**(3*i)",(2,3,1),3)
sound+=2*doCompass(".5","200*("+semitom+")**(3*i)",(3,1,2),3)

sound1=2*doCompass(".5","200*("+semitom+")**(3*i)",(2,3,1),3)
sound1+=2*doCompass(".5","200*("+semitom+")**(3*i)",(3,1,2),3)
sound2=2*doCompass(".5","4*200*("+semitom+")**(3*i)",(2,3,1),3)
sound2+=2*doCompass(".5","4*200*("+semitom+")**(3*i)",(2,3,1),3)

for i,j in zip(sound1,sound2):
    sound.append(i+j)

#sound=[(i+j)*.05 for i,j in ,sound.reverse()]

sound*=2

io=f.IOUtils()
io.recordFile(sound) # grava no audio.wav