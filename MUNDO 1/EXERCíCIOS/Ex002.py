# Ex-002 Crie um programa que leia o dia, o mes e o ano de nascimento de uma pessoa e mostre uma mensagem com a data formatada.

#  Criando 3 variáveis de entrada de dados: dia, mes, ano. Logo após é mostrado uma mensagem na tela, usandos os dados
# inseridos nas mesmas, com f-strings.

dia = input(str('Dia:'))
mes = input(str('Mes:'))
ano = input(str('Ano:'))
print(f'Voce nasceu no dia {dia} de {mes} de {ano}, correto?')