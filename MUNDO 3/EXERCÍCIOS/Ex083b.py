'''
Ex b - Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar
se a expressão passada está com os parênteses abertos e fechados na ordem correta.
'''

# Resposta Professor

expressão = str(input('Digite a expressão: '))
lista = []

for parênteses in expressão:
    if parênteses == '(':  # Para ada '(' ele add em lista
        lista.append('(')
    elif parênteses == ')':  # E Se for ')' , se tiver conteudo dentro de lista ['(']
        if len(lista) > 0:
            lista.pop()  # Ele remove o conteudo para igualar a quantidade de '(' com ')'.
        else:
            pilha.append(')')
if len(lista) == 0:  # Se não tiver ')' em lista a expressão é válida.
    print('Expressão válida!')
else:
    print('Expressão inválida!')  # Senão é inválida pois tem ')' amais!!!
