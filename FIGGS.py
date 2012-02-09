class UnitGrain:
    pass

class Sequence:
    def __init__(self, ordered_grains=[UnitGrain]*3):
        pass

class Permutation:
    def __init__(self, permutation_cycle=(1,2,3)):
        self.permutation_cycle = permutation_cycle

class PermutationPattern(Permutation):
    def __init__(self,periodo_aplicacao=1):
        pass
    
class Run(Grains,PermutationPattern):
    def __init__(self, iterations, Grains, Permutations):
         grains=Grains.number * iterations
    def sythesizeSounds(self):
        pass
    def recordFile(self):
        pass

