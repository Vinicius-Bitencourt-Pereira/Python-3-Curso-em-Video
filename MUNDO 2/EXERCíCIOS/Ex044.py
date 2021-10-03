'''
# Ex- 44 Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
- à vista dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço formal
- 3x ou mais no cartão: 20% de juros
'''
# Centralizanso "LOJAS FALCATRUANAS" em 40 caracteres.
print(f'{" LOJAS FALCATRUANAS ":=^40}')

 # Recebendo o valor da compra.
produto = float(input('Qual o valor da compra?'))

# Imprimindo as formas de pagamento.
print('''FORMAS DE PAGAMENTO:

[1] à vista dinheiro/cheque
[2] à vista no cartão
[3] em até 2x no cartão
[4] 3x ou mais no cartão
''')

# Recebendo a opção de pagamento desejada.
pagamento = int(input('Qual será a forma de pagamento? '))

# Comparando a opção desejada e imprimindo o resultado.
if pagamento == 1 :
  valor = produto - (produto * 10 / 100)
  print(f'O valor de {produto} R$ para pagamentos avista dinheiro/cheque é: {valor} R$ .')
elif pagamento == 2 :
  valor = produto - (produto * 5 / 100)
  print(f'O valor de {produto} R$ para pagamentos avista no cartao é: {valor} R$ . ')
elif pagamento == 3 :
  valor = produto
  print(f'O valor de {produto} R$ para pagamentos em até 2x no cartao é: {valor} R$, valor normal!   ')
elif pagamento == 4 :
  valor = produto + (produto * 20 / 100)
  print(f'O valor de {produto} R$ para pagamentos em 3x ou mais no cartao é: {valor} R$ .  ')
else:
  print('Forma de pagamento invalida, tente novamente!!!')