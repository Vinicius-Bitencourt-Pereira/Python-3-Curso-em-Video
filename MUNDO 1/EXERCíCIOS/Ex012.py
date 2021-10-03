# ex-012 Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

produto = float(input('Digite o valor do produto desejado: '))

# Variável que calcula 5% de produto.
porcentagem = (produto - ((produto * 5) / 100))

print(f'O valar do produto é {produto} R$, e com desconto de 5% fica {porcentagem} R$ .')