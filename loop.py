import csv

with open('contact.csv',mode='r') as contatos:
    leitor = csv.reader(contatos, delimiter=',')
    linhas = 0

    for coluna  in leitor:
        if linhas == 0:
            print(f'Colunas:{" ".join(coluna)}')
            linhas += 1
    else:
        linhas += 2

    print(f'Lidas {linhas} linhas.')