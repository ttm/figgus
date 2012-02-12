import os

os.mkdir('ep-Projeto_Solvente')

#os.chdir('examples')


execfile("examples/try4_B.py")
os.system('mv sound.wav ep-Projeto_Solvente/04-Butano.wav')
print "gravado o arquivo ep-Projeto_Solvente/04-Butano.wav"

execfile("examples/try5_B.py")
os.system('mv sound.wav ep-Projeto_Solvente/05-Tiner.wav')
print "gravado o arquivo ep-Projeto_Solvente/05-Tiner.wav"

execfile("examples/try6_B.py")
os.system('mv sound.wav ep-Projeto_Solvente/06-Tolueno.wav')
print "gravado o arquivo ep-Projeto_Solvente/06-Tolueno.wav"

execfile("examples/try7.py")
os.system('mv both.wav ep-Projeto_Solvente/07-Benzina.wav')
print "gravado o arquivo ep-Projeto_Solvente/07-Benzina.wav"

execfile("examples/try3_B.py")
os.system('mv sound.wav ep-Projeto_Solvente/08-LSA.wav')
print "gravado o arquivo ep-Projeto_Solvente/08-LSA.wav"

execfile("examples/try2.py")
os.system('mv sound.wav ep-Projeto_Solvente/09-Cloroformio.wav')
print "gravado o arquivo ep-Projeto_Solvente/09-Cloroformio.wav"

execfile("examples/try5.py")
os.system('mv sound.wav ep-Projeto_Solvente/10-agua.wav')
print "gravado o arquivo ep-Projeto_Solvente/10-agua.wav"