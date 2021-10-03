# ex-010 Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

# Criando as  variáveis de entrada, do tipo float.
reais = float(input('Quantos reais voce possui em sua carteira? '))
cotacao = float(input('Digite o valor da cotação do dólar hoje? '))

# Variável que recebe o cálculo.
dolar = reais / cotacao

# ' :.2f ' exibe o número com apenas 2 casas decimais.
print(f'Com {reais} R$ você consegue comprar {dolar:.2f} Us$ !')