import csv
from faker import Faker

fake = Faker()
faker = 'pt-BR'

arq_csv = 'teste2.csv'
coluna = ['Nomes']
qnt_registro = 10
tamanho_max = 20

# abrir em modo de escritapara caso nao tenha o arquivo, se crie
with open(arq_csv, 'w', newline='', encoding='utf-8') as arquivo:
    writer = csv.writer(arquivo)

    writer.writerow(coluna)
    
    for i in range(qnt_registro):
        # verifica se o tamanho da palavra gerada é menor que 20
        while True:
            nome_prod = f"{fake.word().capitalize()} {fake.word().capitalize()}"
            if len(nome_prod) <= tamanho_max:
                break   
        # se for menor, escreve     
        writer.writerow([nome_prod])