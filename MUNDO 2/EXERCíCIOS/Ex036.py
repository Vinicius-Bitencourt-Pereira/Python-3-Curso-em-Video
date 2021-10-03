''' Ex- 036: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do
comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado'''

# Criando as variáveis de entrada de dados. ( casa, salario, anos ).
casa = float(input('Qual o valor da casa? '))
salario = float(input('Qual seu salário? '))
anos = float(input('Em quantos anos você pretende pagar? '))

# Variável que recebe o n° de prestações.
prestacao = casa / (anos * 12)

# Checando se a prestação é maior ou menor que 30% do salário.
# Após imprime o resultado.
if prestacao <= ((salario * 30) / 100):
    print(f'Finânciamento APROVADO! o valor da casa é {casa:.2f} R$, seu salário é {salario:.2f} R$, a prestação da casa vai ficar {prestacao:.2f} R$, ou seja 30% ou menos do seu salário.  ')
else:
    print( f'Finânciamento NEGADO! o valor da casa é {casa:.2f} R$, seu salário é {salario:.2f} R$, a prestação da casa vai ficar {prestacao:.2f} R$, ou seja 30% ou mais do seu salário.  ')
    print('Ifelizmente você não conseguiu se encaixar em todos os critérios nessessários para o finânciamento do seu imóvel! ')
