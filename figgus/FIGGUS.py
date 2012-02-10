###### THE BASIC SEQUENCE: ######

from tables import *

class UnitGrain:
	"""Sonic minimum unit, be it a grain or a note
	
	Write something about phonons and granular synthesis.
	(Gabor and Roads)"""
	def __init__(self,duration=1,freq=220,timbre=0,intensidade=1,fades=0):
        	self.duration=duration
	        self.freq=freq
	        self.timbre=timbre
	        self.intensidade=intensidade
	        self.fades=fades
        

class Sequence:
    """Sequence of sonic atoms, our 'UnitGrain' classes"""
    def __init__(self, ordered_unit_grains=[UnitGrain()]*3):
        self.ordered_unit_grains=ordered_unit_grains
        self.unit_count=len(ordered_unit_grains)
        self.active_grains=range(self.unit_count)


class Permutation:
    """Simple permutation.
    
    see http://en.wikipedia.org/wiki/Permutation for nomenclature
    
    If one-line notation, it runs like:
    permuted=[original[i] for i in Permutation.one_line]
    
    If cycle notation:
    unfold to one-line notation
    
    note
    one_line = (2,3,1) # is equivalent to
    cycle=(1,2,3)
    
    one_line=(2,5,4,3,1) # is equivalent to
    cycle=(1,2,5)(3,4)"""
    def __init__(self, one_line=(2,3,1)):
        self.one_line = one_line
        

class PermutationPattern(Permutation):
    """A Permutation with periodicity/incidence_index information"""
    period=1
    def changePeriodicity(self, new_val=1):
	self.period=new_val


class Pattern:
    """Sequence with PermutationPattern classes applied successively
    
    Parameters
    ----------
    sequence : class
      An instantiated FIGGUS Sequence class
    permutation_pattern : class
      An instantiated FIGGUS PermutationPattern class"""
    def __init__(self, iterations=1, sequence=Sequence(), permutation_pattern=PermutationPattern()):
        self.unit_count=sequence.unit_count * iterations
        self.sequence=sequence
        self.permutation_pattern=permutation_pattern
        
        pattern=[sequence.active_grains]
        stage=sequence.active_grains
	for i in xrange(iterations):
	    if i%permutation_pattern.period == 0:
		stage = [stage[i-1] for i in permutation_pattern.one_line]
		pattern.append(stage)
	    else:
		pattern.append(stage)
	self.pattern=pattern # lista de listas que sao as posicoes em cada compasso
	self.initFileSpecs()

    def initFileSpecs(self):
	self.SR=44100
	self.N=1024 #utilizado na classe Tables

    def synthesizeSonicVectors(self):
	sonic_vector=[]
	
	for compass in self.pattern:
	    units=[ self.sequence.ordered_unit_grains[position] for position in compass]
	    compass_vector=[]
	    for unit in units:
		SI= unit.freq * self.N / self.SR
		ap=0
		for i in xrange(int(unit.duration*self.SR)):
		    sonic_vector.append(unit.intensidade*Tables.sin1024[int(ap)])
		    ap = (SI + ap)%self.N
	self.sonic_vector=sonic_vector

class Tables:
    f=open("tables/sin1024.txt","r")
    sin1024=[float(i) for i in f.read().split(",")]
    f.close()
    
    f=open("tables/sin2048.txt","r")
    sin2048=[float(i) for i in f.read().split(",")]
    f.close()
    
    f=open("tables/saw1024.txt","r")
    saw1024=[float(i) for i in f.read().split(",")]
    f.close()
    
    f=open("tables/saw2048.txt","r")
    saw2048=[float(i) for i in f.read().split(",")]
    f.close()
    
    f=open("tables/wnoise1024.txt","r")
    wnoise1024=[float(i) for i in f.read().split(",")]
    f.close()
    
    f=open("tables/wnoise2048.txt","r")
    wnoise2048=[float(i) for i in f.read().split(",")]
    f.close()

import wave, struct
#class PatternPlayer(Pattern):
class IOUtils:
    def recordPattern(self,filename,pattern):
	self.recordFile(filename,pattern.sonic_vector,pattern.SR)
	
    def recordFile(self,filename="sound.wav",sonic_vector=[], samplerate=44100):
	sound = wave.open(filename,'w')
	sound.setframerate(samplerate)
	sound.setnchannels(1) # Always Mono
	sound.setsampwidth(2) # Always 16bit/sample (2 bytes)

	sonic_vector=self.boundVector(sonic_vector)

	sonic_vector=[i*(2**15-1) for i in sonic_vector] #signed 16 bit
	sound.writeframes(struct.pack('h'*len(sonic_vector),*[int(i) for i in sonic_vector]))
	sound.close()

    def boundVector(self,vector):
	"""Bound vector in the [-1,1] interval"""
	svmin=min(vector)
	svmax=max(vector)
	ambit=svmax-svmin
	if svmax>1 or svmin<-1:
	    if svmax-svmin > 2:
		i=0
		for sample in vector:
		    new_sample=(sample-svmin)/ambit # results in [0,1]
		    new_sample=new_sample*2-1 # results in [-1,1]
		    vector[i]=new_sample
		    i+=1
	    elif svmax > 1:
		offset=svmax-ambit/2
		i=0
		for sample in vector:
		    new_sample=sample - offset
		    vector[i]=new_sample
		    i+=1
	    elif svmin < -1:
		offset=-svmin -ambit/2
		i=0
		for sample in vector:
		    new_sample=sample + offset
		    vector[i] = new_sample
		    i+=1
	return vector
