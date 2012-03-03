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
def doCompass():
    for i in xrange(n):
	s.ordered_unit_grains[i].freq=10000 - 1000*(i+1)
	s.ordered_unit_grains[i].duration=.2 + 0.05*i
	#print 100*(i+1)
	
    s.ordered_unit_grains[1].freq=100
    s.ordered_unit_grains[3].freq=500
	
    #pp=PermutationPattern()
    p=f.Pattern(s,f.PermutationPattern(),8)
    p.synthesizeSonicVectors()
    return p.sonic_vector

sound+=doCompass()

# COMPASS 5-8 *.*.*.*.*.*.*.*.*.*.*.*.* 2
"""for i in xrange(n):
    s.ordered_unit_grains[i].freq=10000 - 1000*(i+1)
    s.ordered_unit_grains[i].duration=.2# + 0.05*i
    #print 100*(i+1)
    
s.ordered_unit_grains[1].freq=100
s.ordered_unit_grains[3].freq=500
    
#pp=PermutationPattern()
p=f.Pattern(s,f.PermutationPattern(),8)
p.synthesizeSonicVectors()
sound+=p.sonic_vector


# COMPASS 9-12 *.*.*.*.*.*.*.*.*.*.*.*.* 3
for i in xrange(n):
    s.ordered_unit_grains[i].freq=10000 - 1000*(i+1)
    s.ordered_unit_grains[i].duration=.05*i#.2# + 0.05*i
    #print 100*(i+1)
    
s.ordered_unit_grains[1].freq=100
s.ordered_unit_grains[3].freq=500
    
#pp=PermutationPattern()
p=f.Pattern(s,f.PermutationPattern(),8)
p.synthesizeSonicVectors()
sound+=p.sonic_vector

###################

# COMPASS 13-16 *.*.*.*.*.*.*.*.*.*.*.*.* 4
for i in xrange(n):
    s.ordered_unit_grains[i].freq=10000 - 1000*(i+1)
    s.ordered_unit_grains[i].duration=.1#.2# + 0.05*i
    #print 100*(i+1)
    
s.ordered_unit_grains[1].freq=100
s.ordered_unit_grains[3].freq=500
    
#pp=PermutationPattern()
p=f.Pattern(s,f.PermutationPattern(),8)
p.synthesizeSonicVectors()
sound+=p.sonic_vector

########## 4 compassos de 4 1
##########
##########
# COMPASS 1-4 *.*.*.*.*.*.*.*.*.*.*.*.* 1
for i in xrange(n):
    s.ordered_unit_grains[i].freq=10000 - 1000*(i+1)
    s.ordered_unit_grains[i].duration=.2 + 0.05*i
    #print 100*(i+1)
    
s.ordered_unit_grains[1].freq=100
s.ordered_unit_grains[3].freq=500*3./2 ### Uma quinta a cima o pedal/bola
    
#pp=PermutationPattern()s
p=f.Pattern(s,f.PermutationPattern(),8)
p.synthesizeSonicVectors()
sound+=p.sonic_vector


# COMPASS 5-8 *.*.*.*.*.*.*.*.*.*.*.*.* 2
for i in xrange(n):
    s.ordered_unit_grains[i].freq=10000 - 1000*(i+1)
    s.ordered_unit_grains[i].duration=.2# + 0.05*i
    #print 100*(i+1)
    
s.ordered_unit_grains[1].freq=100
s.ordered_unit_grains[3].freq=500*3./2 ### Uma quinta a cima o pedal/bola
    
#pp=PermutationPattern()
p=f.Pattern(s,f.PermutationPattern(),8)
p.synthesizeSonicVectors()
sound+=p.sonic_vector


# COMPASS 9-12 *.*.*.*.*.*.*.*.*.*.*.*.* 3
for i in xrange(n):
    s.ordered_unit_grains[i].freq=10000 - 1000*(i+1)
    s.ordered_unit_grains[i].duration=.01*i**2#.2# + 0.05*i
    #print 100*(i+1)
    
s.ordered_unit_grains[1].freq=100
s.ordered_unit_grains[3].freq=500*3./2 ### Uma quinta a cima o pedal/bola
    
#pp=PermutationPattern()
p=f.Pattern(s,f.PermutationPattern(),8)
p.synthesizeSonicVectors()
sound+=p.sonic_vector

###################

# COMPASS 13-16 *.*.*.*.*.*.*.*.*.*.*.*.* 4
for i in xrange(n):
    s.ordered_unit_grains[i].freq=10000 - 1000*(i+1)
    s.ordered_unit_grains[i].duration=.1#.2# + 0.05*i
    #print 100*(i+1)
    
s.ordered_unit_grains[1].freq=100
s.ordered_unit_grains[3].freq=500*3./2 ### Uma quinta a cima o pedal/bola
    
#pp=PermutationPattern()
p=f.Pattern(s,f.PermutationPattern(),4)
p.synthesizeSonicVectors()
sound+=p.sonic_vector

#########
#########
######### 4 compass de 4 ::: 2

# COMPASS 1-4 *.*.*.*.*.*.*.*.*.*.*.*.* 1
for i in xrange(n):
    s.ordered_unit_grains[i].freq=10000 - 1000*(i+1)
    s.ordered_unit_grains[i].duration=.2 + 0.05*i
    #print 100*(i+1)
    
s.ordered_unit_grains[1].freq=100
s.ordered_unit_grains[3].freq=500/2
    
#pp=PermutationPattern()
p=f.Pattern(s,f.PermutationPattern(),8)
p.synthesizeSonicVectors()
sound+=p.sonic_vector


# COMPASS 5-8 *.*.*.*.*.*.*.*.*.*.*.*.* 2
for i in xrange(n):
    s.ordered_unit_grains[i].freq=10000 - 1000*(i+1)
    s.ordered_unit_grains[i].duration=.2# + 0.05*i
    #print 100*(i+1)
    
s.ordered_unit_grains[1].freq=100
s.ordered_unit_grains[3].freq=500/2
    
#pp=PermutationPattern()
p=f.Pattern(s,f.PermutationPattern(),8)
p.synthesizeSonicVectors()
sound+=p.sonic_vector


# COMPASS 9-12 *.*.*.*.*.*.*.*.*.*.*.*.* 3
for i in xrange(n):
    s.ordered_unit_grains[i].freq=10000 - 1000*(i+1)
    s.ordered_unit_grains[i].duration=.2*i#.2# + 0.05*i
    #print 100*(i+1)
    
s.ordered_unit_grains[1].freq=100
s.ordered_unit_grains[3].freq=500/2
    
#pp=PermutationPattern()
p=f.Pattern(s,f.PermutationPattern(),8)
p.synthesizeSonicVectors()
sound+=p.sonic_vector

###################

# COMPASS 13-16 *.*.*.*.*.*.*.*.*.*.*.*.* 4
for i in xrange(n):
    s.ordered_unit_grains[i].freq=10000 - 1000*(i+1)
    s.ordered_unit_grains[i].duration=.1*i#.2# + 0.05*i
    #print 100*(i+1)
    
s.ordered_unit_grains[1].freq=100
s.ordered_unit_grains[3].freq=500/2
    
#pp=PermutationPattern()
p=f.Pattern(s,f.PermutationPattern(),8)
p.synthesizeSonicVectors()
sound+=p.sonic_vector


########
########
######## Acabou 3 x 4 compass de 4 == tonica dominante tonica


io=f.IOUtils()
io.recordFile("som.wav",sound)

#print "== Ouca que 'o triangulo gira e existe uma bola do lado' (nome da peca) =="
"""