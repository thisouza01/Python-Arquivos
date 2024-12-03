import os

# O diretorio a ser deletado tem que estar vazio
diretorio = 'DiretorioB'

diretorioPai = 'C:\Diretorios\Teste'

path = os.path.join(diretorioPai, diretorio)

# se estiver vazio ele deleta se nao gera um erro
os.rmdir(path)
