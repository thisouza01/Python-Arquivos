import os

# pegar diretório de trabalho atual
# cwd = os.getcwd()

# mostrar diretório atual
# print(cwd)

def caminho_atual ():
    print('Diretório de trabalho atual')
    print(os.getcwd())
    print()

# usa função caminho atual 
caminho_atual()

# altera caminho atual
os.chdir('../')

# usa função caminho atual
caminho_atual()