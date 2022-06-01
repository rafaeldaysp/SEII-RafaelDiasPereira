import csv

with open('arquivo.csv', 'w') as f:
    
    for i in range(10):
        csv.writer(f, delimiter='\t').writerow(('Rafael Days', '11911EAU003', 'Engenharia de Controle e Automacao'))
        

with open('arquivo.csv', 'r') as f:
    for linha in csv.DictReader(f, fieldnames=('Nome', 'Matricula', 'Curso'), delimiter='\t'):
        print(linha)
        print(linha['Nome'])