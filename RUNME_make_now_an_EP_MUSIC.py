import os

def exec_(fname):
    os.system("python3 "+fname)

if not os.path.isdir('ep-Projeto_Solvente'):
    os.mkdir('ep-Projeto_Solvente')

exec_("./examples/triangulo3_B.py")
os.system('mv sound.wav ep-Projeto_Solvente/01-Eter.wav')
print("gravado o arquivo 'ep-Projeto_Solvente/01-Eter.wav'")

exec_("examples/try4_B.py")
os.system('mv sound.wav ep-Projeto_Solvente/04-Butano.wav')
print("gravado o arquivo 'ep-Projeto_Solvente/04-Butano.wav'")

exec_("examples/try5_B.py")
os.system('mv sound.wav ep-Projeto_Solvente/05-Thinner.wav')
print("gravado o arquivo 'ep-Projeto_Solvente/05-Thinner.wav'")

exec_("examples/try6_B.py")
os.system('mv sound.wav ep-Projeto_Solvente/06-Tolueno.wav')
print("gravado o arquivo 'ep-Projeto_Solvente/06-Tolueno.wav'")

exec_("examples/try7.py")
os.system('mv both.wav ep-Projeto_Solvente/07-Benzina.wav')
print("gravado o arquivo 'ep-Projeto_Solvente/07-Benzina.wav'")

exec_("examples/try3_B.py")
os.system('mv sound.wav ep-Projeto_Solvente/08-LSA.wav')
print("gravado o arquivo 'ep-Projeto_Solvente/08-LSA.wav'")

exec_("examples/try2.py")
os.system('mv sound.wav ep-Projeto_Solvente/09-Cloroformio.wav')
print("gravado o arquivo 'ep-Projeto_Solvente/09-Cloroformio.wav'")

exec_("examples/try5.py")
os.system('mv sound.wav ep-Projeto_Solvente/10-Agua.wav')
print("gravado o arquivo 'ep-Projeto_Solvente/10-Agua.wav'")
