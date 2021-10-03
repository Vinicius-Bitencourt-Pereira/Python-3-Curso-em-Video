'''
Ex 80.b: Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição
 correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.

'''
# Resposta Guanabara

lista = []

for x in range(5):
    valor = int(input('Digite um valor: '))
    # Se x for o primeiro ou maior que o ultimo número da lista, adicionamos ao final da lista.
    if x == 0 or valor > lista[-1]:
        lista.append(valor)
        print('Adicionado ao final da lista...')
    else:
        posição = 0
        while posição < len(lista):
            if valor <= lista[posição]:
                lista.insert(posição, valor)
                print(f'Adicionado na posição {posição} da lista...')
                break
            posição += 1
print('==' * 30)
print(f'Os valores digitados em ordem foram {lista}')
