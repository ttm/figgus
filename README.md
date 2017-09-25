# FIGGS: Finite Groups in Granular and Unit Synthesis

This is a rewriting of the old 'FIGGS': Finite Groups in Granular and Unit Synthesis.
It does not contain all the possibilities of the original implementation
(which also had a fancy GUI).
A more complete implementation of such techniques should
be found at the [MASS](https://github.com/ttm/mass)
framework and at the 
[MUSIC](https://github.com/ttm/music) Python package.

This package should be usable in both Python 2 and 3.
Install it with the usual:
  $ python setup.py install

Or, to ease tweaking:
  $ git clone https://github.com/ttm/figgus
  $ sudo pip install -e <path_to_repo>

Make the PPEPPS musical pieces running the script:
  $ python runme_make_ep.py

Should 
See files and TODO for now, or write us:
labmacambira@googlegroups.com
renato.fabbri@gmail.com

Or try the IRC channel:
#labmacambira @ irc.freenode.net


### notes
FIGGUS is a very early usage of the
[MASS framework](https://github.com/ttm/mass)
to render a musical album.
It is relevant because:
* It uses MASS but does not require Numpy to render sonic arrays and write WAV files.
* Implements a whole EP album ([PPEPPS]).
* Inherits the original FIGGUS concepts [1][2].
* Is a step betwen original FIGGUS and the music package.

[1]: Fabbri, R. and Maia Jr, A. “Applications of Group Theory on Granular Synthesis”. Annals of the
VIII Brazilian Symposium on Computer Music, 109-120, 2007.
[2]: Fabbri, Renato, and Adolfo Maia Jr. "Applications of group theory on sequencing and spatialization of granular sounds." 6º Congresso de Engenharia de Áudio. 2008.

Beyond curiosity and the [PPEPPS],
one should look at the [MASS] framework
or the [Music] Python package.

[PPEPPS]: 
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




