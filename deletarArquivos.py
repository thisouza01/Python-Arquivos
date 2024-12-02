# usando os.remove() os.rmdir()
# os.remove() -> Remove ou deleta um caminho de arquivo (nao remove ou deleta diretorios)

import os

# arquivo que vai ser excluido
arquivo = 'arquivo1.txt'

# localização do arquivo
local = 'c:\Diretorios'

# junção dos caminhos
path = os.path.join(local, arquivo)

# remove arquivo
os.remove(path)