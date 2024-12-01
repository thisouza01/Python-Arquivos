import os

# nome do diretorio que vai criar
diretorio1 = 'CriaDiretorio1'

# diretorio pai
diretorio_pai1 = "C:\Python-Arquivos"

# junta caminho
path1 = os.path.join(diretorio_pai1, diretorio1)

# cria diretorio
os.mkdir(path1)
print(f'Diretorio {diretorio1} foi criado!')
print()

# segundo forma de criar um diretorio
diretorio2 = 'CriaDiretorio2'

diretorio_pai2 = "C:\Python-Arquivos"

# modo
modo = 0o666
path2 = os.path.join(diretorio_pai2, diretorio2)

os.mkdir(path2, modo)
print(f'Diretorio {diretorio2} foi criado!')