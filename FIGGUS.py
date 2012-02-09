###### THE BASIC SEQUENCE: ######
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
		    sonic_vector.append(unit.intensidade*Tables.sin_cycle[int(ap)])
		    ap = (SI + ap)%self.N
	self.sonic_vector=sonic_vector
	    
import numpy as n

class Tables:
    sin_cycle=n.sin(n.linspace(0,n.pi*2,1024,endpoint=False))
    ramp_cycle=n.linspace(-1,1,1024)
    tri_cycle=n.hstack((ramp_cycle[::2],ramp_cycle[-1:1:2]))
    white_noise=n.random.random(1024)*2-1

import wave, struct
#class PatternPlayer(Pattern):
class PatternPlayer():
	
        
    def recordFile(self):
	sound = wave.open('sinusoid.wav','w')
	sound.setnchannels(1) # Mono
	sound.setframerate(44100) # 44.1k
	# Numero de bytes do arquivo, estamos pensando em 16 bits, 2 bytes, certo?!
	sound.setsampwidth(2) # 16bit/sample (2 bytes)
	sonic_vector=((n.sin(n.linspace(0,5*220*(2*n.pi),44100*5)))*.5    )*(2**16)
	sound.writeframes(struct.pack('h'*44100*5,*[int(i) for i in sonic_vector]))
	sound.close()