import figgus as f

n=3
grains=[f.UnitGrain(),f.UnitGrain(),f.UnitGrain()]
s=f.Sequence(grains)

def doCompass(durs,freqs,perms,ncomps):
    for i in xrange(n):
	s.ordered_unit_grains[i].freq=eval(freqs)
	s.ordered_unit_grains[i].duration=eval(durs)
	print 1*(i+1)

    p=f.Pattern(s,f.PermutationPattern(perms),ncomps)
    p.synthesizeSonicVectors()
    return p.sonic_vector

semitom = "2**(1/12.)" # multiplication factor, 12 semintons gives an octave: 2 doubles de freqs
dur=".3"
sound=[]

######


sounda=doCompass(dur,"200*("+semitom+")**(4*i)",(2,1),2*4)
soundb=doCompass(dur,"200*(6./2.)*("+semitom+")**(4*i)",(2,1),2*4)
#soundb=doCompass(dur,"200*("+semitom+")**(4*i)",(2,3,1),3*4)
sound = sounda#+soundb

stemp3=[(i+j)*.5 for i,j in zip(sounda,soundb)]
sound += stemp3

soundc=doCompass(dur,"300*4*(6./2.)*("+semitom+")**(4*i)",(3,1,2),2*4)
stemp4=[(i+j+k)*.32 for i,j,k in zip(sounda,soundb,soundc)]
sound+=stemp4

soundd=doCompass(dur,"300*4*(6./2.)*("+semitom+")**(4*i)",(2,3,1),2*4)
stemp5=[(i+j+k)*.32 for i,j,k in zip(sounda,soundb,soundd)]
sound+=stemp5

sounde=doCompass(dur,"100*("+semitom+")**(4*i)",(2,1),2*4)
sound+=sounde


#sounda1=doCompass(dur,"100*("+semitom+")**(3*i)",(3,1,2),3*4)
#soundb1=doCompass(dur,"200*(2/3.)*("+semitom+")**(3*i)",(2,3,1),3*4)
#stemp = [(i+j)*.5 for i,j in zip(sounda1,soundb1)]
#sound += stemp

#sound += sounda1+soundb1

#stemp2 = [(i+j)*.5 for i,j in zip(sounda,soundb)]
#stemp3 = [(i+j)*.5 for i,j in zip(stemp,stemp2)]
#sound += 2*stemp3

io=f.IOUtils()
io.recordFile(sound) #records a mono 16 bit

print "\n== triangulo gira em crescente ==\n"

#
# 123
# 213
# 231
# 321
# 312
# 132

# c3
# 123
# 231
# 312
# -c3
# 123
# 312
# 231

"""
sound1B=doCompass(dur,"4*200*("+semitom+")**(3*i)",(2,3,1),3)
sound1C=doCompass(dur,".5*200*("+semitom+")**(3*i)",(2,3,1),3)
sound2=doCompass(dur,"200*("+semitom+")**(3*i)",(3,1,2),3) # Inverting quirality
sound2B=doCompass(dur,"4*200*("+semitom+")**(3*i)",(3,1,2),3) # Inverting quirality
sound2C=doCompass(dur,".5*200*("+semitom+")**(3*i)",(3,1,2),3) # Inverting quirality
silencio=doCompass(dur,"0",(2,3,1),1)



#left=[(i+j+k)*.32 for i,j,k in zip(sound1,sound2B,sound1C,)]
#right=[(i+j+k)*.32 for i,j,k in zip(sound2,sound1B,sound2C)]
left=left1=[(i+j+k)*.32 for i,j,k in zip(sound1,sound1B,sound1C,)]
right=right1=[(i+j+k)*.32 for i,j,k in zip(sound1,sound1B,sound1C)]
left += left1 + right1
right += right1+ left1

left*=2
right*=2

#left2=[(i+j+k)*.32 for i,j,k in zip(sound1,sound1B,sound2C,)]; left+=left2
#right2=[(i+j+k)*.32 for i,j,k in zip(sound2,sound2B,sound1C)]; right+=right2
#left+=right2
#right+=left2

#left30=[(i+j+k)*.32 for i,j,k in zip(sound1,sound2B,sound2C)]; left+=left30
#right30=[(i+j+k)*.32 for i,j,k in zip(sound2,sound2B,sound1C)]; right+=right30
#left+=right30
#right+=left30


left3=[(i+j+k)*.32 for i,j,k in zip(sound2,sound2B,sound2C)]
right3=[(i+j+k)*.32 for i,j,k in zip(sound2,sound2B,sound1C)]
left+=left3+right3
right+=right3+left3

#####====

L=len(sound2)
left33= sound2[:L/3]+sound2B[L/3:2*L/3]+sound2C[2*L/3:] # Sobe
right33=sound2C[:L/3]+sound2[L/3:2*L/3]+sound2B[2*L/3:] # Desce
left+=left33+right33
right+=right33+left33

left4= sound1[:L/3]+sound1C[L/3:2*L/3]+sound1B[2*L/3:] # Sobe
right4=sound1B[:L/3]+sound1[L/3:2*L/3]+sound1C[2*L/3:] # Sobe
left+=(left4+right4)            *                  2 
right+=(right4+left4)           *                  2

left5= sound1[:L/3]+sound1B[L/3:2*L/3]+sound1C[2*L/3:] # Desce
right5=sound1B[:L/3]+sound1C[L/3:2*L/3]+sound1[2*L/3:] # Desce
left+=(left5+right5)            *                  2
right+=(right5+left5)           *                  2

left6= sound2[:L/3]+sound2B[L/3:2*L/3]+sound2C[2*L/3:] # Desce
right6=sound2C[:L/3]+sound2B[L/3:2*L/3]+sound2[2*L/3:] # Sobe
left+=left6+right6
right+=right6+left6

#####====




left+=left3
right+=right3
left+=right3
right+=left3

######

io=f.IOUtils()
#io.recordFile(left,[],"left.wav") #records a mono 16 bit
#io.recordFile(right,[],"right.wav") #records a mono 16 bit
io.recordFile(left,right,"both.wav") #records a mono 16 bit"""