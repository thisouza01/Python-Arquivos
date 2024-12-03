import os

# mostra nome do sistema operacional 
print(os.name)
print()

try:
    nomeArquivo = 'arquivo2'
    # abre arquivo mode de leitura padrão
    arquivo = open(nomeArquivo, 'r')
    # le o texto
    texto = arquivo.read()
    # fecha arquivo
    arquivo.close()
except IOError:
    print('Problema de leitura: ' + nomeArquivo)    