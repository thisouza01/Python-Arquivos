import os

nomeArquivo = 'arquivo2'

# abre arquivop em modo de escrita
arquivo = open(nomeArquivo, 'w')
# escreve no arquivo
arquivo.write("Olá")

arquivo.close()

arquivo = open(nomeArquivo, 'r')

texto = arquivo.read()

print(texto)
print()

arquivo = os.popen(nomeArquivo, 'w')

arquivo.write("Mundo")

