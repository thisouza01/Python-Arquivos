# importa modulo csv
import csv

# criar arquivo csv
# caso não tenha criado ainda, abrir no modo "w" faz com que ele crie e abra em modo de escrita
with open('teste1.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    writer.writerow(['nome', 'idade'])
    writer.writerow(['Thiago','22'])
    writer.writerow(['Joao','20'])
    writer.writerow(['Pedro','21'])

