cp = 0
while cp < 10:
    cp += 1

    if cp == 3 or cp == 5: # Não exibe o 3 e o 5
        continue           # Não exibe e continua os próximos

    if cp == 7: # Não exibe o 7
        break   # Para aqui

    print(f'Produto {cp}')

# while decrescente de 4 até 1
i = 4
while i > 0:
    print(i)
    i -= 1