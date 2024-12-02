# os.makedirs() cria até os diretorios passados que não existem

import os

diretorioA = 'DiretorioA'
diretorioPaiA = 'C:\Diretorios'

pathA = os.path.join(diretorioPaiA, diretorioA)

os.makedirs(pathA)

print(f'Diretorio "{diretorioA}" criado!')

diretorioB = 'DiretorioB'
# diretorio que nao foi criado ainda "Teste"
diretorioPaiB = 'C:\Diretorios\Teste'
modo = 0o666

pathB = os.path.join(diretorioPaiB, diretorioB)

os.makedirs(pathB, modo)

print(f'Diretorio "{diretorioB}" criado!')
