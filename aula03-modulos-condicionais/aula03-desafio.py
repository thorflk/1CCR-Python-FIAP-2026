idade = int(input('Informe sua idade: '))

if idade < 16:
    print('Não pode votar')

elif (idade >= 16 and idade < 18) or idade > 70:
    print('O voto é opcional')

else:
    print('O voto é obrigatório')