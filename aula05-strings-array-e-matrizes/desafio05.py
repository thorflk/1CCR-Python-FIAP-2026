lista_nomes = ['Ana', 'Bia', 'Alex', 'Caio']

for i in range(len(lista_nomes)):
    for j in range(i + 1, len(lista_nomes)):
        print(f'{lista_nomes[i]} e {lista_nomes[j]}')