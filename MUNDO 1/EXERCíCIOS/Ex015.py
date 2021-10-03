'''
ex-015 Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade
de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
'''

# Variável que recebe os dias pelo usuário.
dias = float(input('Quantos dias você ficou com o veículo? '))

# Variável que calcula o valor da diária.
vdia = 60 * dias

# Variável que recebe a quilometragem.
km = float(input('Quantos km você rodou com o veículo? '))

# Variável que calcula o valor da quilometragem.
vkm = 0.15 * km

print(f'Voce rodou {km} km em {dias} dias, o valor total de sua despesa é de {vdia + vkm } R$ . ')
