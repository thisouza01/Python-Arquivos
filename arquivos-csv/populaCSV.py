import csv
from faker import Faker

# lingua que criará os nomes
faker = Faker('pt-BR')

# nome do arquivo csv
arq_csv = 'teste1.csv'

# define a coluna do arquivo
coluna = ['Nome']

# define quantidade de registros
qnt_registro = 10

# abre csv em modo de escrita
with open(arq_csv, 'w', newline='', encoding='utf-8') as arquivo:
    writer = csv.writer(arquivo)

    # cabeçalho
    writer.writerow(coluna)

    # registro
    for _ in range(qnt_registro):
        writer.writerow([
            faker.name()
        ])

print(f"Arquivo {arq_csv} criado com sucesso com {qnt_registro} registros!")        