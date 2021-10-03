'''
Ex 80.a: Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição
 correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.

'''
# Resposta com 2 listas...

lista = []
nova_lista = []

# Criando um loop para Receber os 5 valores de lista[]

for x in range(5):
    valor = int(input('Digite um número: '))
    lista.append(valor)

# Adicionando sempre o novo mínimo de lista à nova_lista
# Criando  um loop para receber o menor valor de lista[] e armazenar em nova_lista[].
# Depois remover o min(lista) para ele receber o novo mínimo a cada loop.

for x in range(len(lista)):
    menor = min(lista)
    nova_lista.append(menor)
    lista.remove(menor)
print(nova_lista)
