'''
Ex- 34 Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
'''

# Recebendo o salário do usuário.
salario = float(input('Digite seu salário: '))

# Para salários <= RS 1250.00, o aumento é de 15% .
aumento_maior = (salario + ((salario * 15) / 100))

# Para salários > RS 1250.00, o aumento é de 10% .
aumento_menor = (salario + ((salario * 10) / 100))

# Verificando se salario é menor ou igual a R$ 1250.00. apos imprime o resultado.
if salario <= 1250.00 :

  print(f'Seu salário atual é de {salario:.2f} R$.')
  print(f'Seu salário com almento será de {aumento_maior:.2f} R$.')
else:
  print(f'Seu salário atual é de {aumento_menor:.2f} R$.')
  print(f'Seu salário com almento será de {salario + (salario * 10) / 100:.2f} R$.')