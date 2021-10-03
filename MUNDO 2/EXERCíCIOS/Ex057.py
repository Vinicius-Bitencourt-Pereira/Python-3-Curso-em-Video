'''
Ex- 57: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso
esteja errado, peça a digitação novamente até ter um valor correto.
'''

# Variável masculino recebe o valor M
masculino = 'M'

# Variável feminino recebe o valor F
feminino = 'F'

# Vriável sexo recebe um valor vazio para início do loop.
sexo = ''

# Enquanto o sexo for diferente de M ou F, o loop ficca ativo.
while sexo != masculino and sexo != feminino:
    # Recebendo o valor de sexo pelo usuário.
    sexo = input('Qual o sexo da pessoa [M/F]? ').upper()
    # Só imprime a mensagem dizendo o sexo do usuário, e esncerra o loop se a mensagem for M ou F .
    if sexo == 'M' or sexo == 'F' :
        print(f'Sexo {sexo} registrado com sucesso!')
    # Caso contrário pede uma opção válida.
    else:
       print('Digite uma opção válida!')