###### THE BASIC SEQUENCE: ######
class UnitGrain:
	"""Sonic minimum unit, be it a grain or a note
	
	Write something about phonons and granular synthesis.
	(Gabor and Roads)"""
	def __init__(self,duration=1,freq=0,timbre=0,intensidade=0,fades=0):
        	self.duration=duration
	        self.freq=0
	        self.timbre=timbre
	        self.intensidade=intensidade
	        self.fades=fades
        

class Sequence:
    """Sequence of sonic atoms, our 'UnitGrain' classes"""
    def __init__(self, ordered_grains=[UnitGrain()]*3):
        self.ordered_grains=ordered_grains
        self.number=len(ordered_grains)


class Permutation:
    def __init__(self, permutation_cycle=(1,2,3)):
        self.permutation_cycle = permutation_cycle

class PermutationPattern(Permutation):
    def __init__(self,periodo_aplicacao=1):
        pass


class Pattern(Sequence,PermutationPattern):
    def __init__(self, iterations, Sequence, PermutationPattern=None):
         grains=Sequence.number * iterations

import numpy as n

class tables:
    sin_cycle=n.sin(n.linspace(0,n.pi*2,1024,endpoint=False))
    ramp_cycle=n.linspace(-1,1,1024)
    tri_cycle=n.hstack((ramp_cycle[::2],ramp_cycle[-1:1:2]))
    white_noise=n.random.random(1024)*2-1

import wave, struct
#class PatternPlayer(Pattern):
class PatternPlayer():
    def sythesizeSonicVectors(self):
	sound = wave.open('sinusoid.wav','w')
	sound.setnchannels(1) # Mono
	sound.setframerate(44100) # 44.1k
	# Numero de bytes do arquivo, estamos pensando em 16 bits, 2 bytes, certo?!
	sound.setsampwidth(2) # 16bit/sample (2 bytes)
	sonic_vector=((n.sin(n.linspace(0,5*220*(2*n.pi),44100*5)))*.5    )*(2**16)
	sound.writeframes(struct.pack('h'*44100*5,*[int(i) for i in sonic_vector]))
	sound.close()
        
    def recordFile(self):
        pass

