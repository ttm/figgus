# FIGGS: Finite Groups in Granular and Unit Synthesis

This is a rewriting of the old 'FIGGS': Finite Groups in Granular and Unit Synthesis.

Install it with the usual:
  $ python3 setup.py install

Make the PPEPPS musical pieces running the script:
  $ python3 runme_make_ep.py

See files and TODO for now, or write us:
labmacambira@googlegroups.com
renato.fabbri@gmail.com

Or try the IRC channel:
#labmacambira @ irc.freenode.net


### notes
For now, FIGGUS is structured as follows:

1) Sonic Material
class UnitGrain is a sonic grain/event
class Sequence takes a sequence of UnitGrain classes in a specific order

2) Permutations
class Permutation is a permutation with some facilities for displaying notation and alterations
class PermutationPattern is a permutation with some more info, like periodicity

3) Resulting Patterns
class Pattern is where the grains and the permutations entangle and where the synthesis come to life

4) Utils
class Tables (in tables.py) reads tables for lookup from directory tables/
class IOUtils is dedicated to easy pattern and vectors IOs

some more elaborated Finite Group stuff should come soon, probrably via gap.

### usage:
import figgus as f

p=f.Pattern() # Pattern uses standard 1s 220Hz sonic units and (123) == [231] permutations
p.synthesizeSonicVectors() #  # makes the sonic vector and stores it in p.sonic_vector

io=f.IOUtils() # instantiates a IO class
io.recordPattern("som.wav",p) # Make .wav from pattern p please :-)


### FIGGS/FIGGUS ancient code:
http://www.estudiolivre.org/el-gallery_view.php?arquivoId=7959


=== /\/\/\/\/\ _o_o_ oOo _o_o_ /\/\/\/\/\ ===




