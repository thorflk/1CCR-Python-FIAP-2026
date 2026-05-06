# matriz = [[(i * 5) + j + 1 for j in range(5)] for i in range(4)]
#
# for linha in matriz:
#     print(linha)

musicas = [
    ['Baby', 'Justin Bieber'],
    ['Umbrella', 'Rihanna'],
    ['Mágica', 'Calcinha Preta']
]

for musica in musicas:
    for info in musica:
        print(info)
    print()