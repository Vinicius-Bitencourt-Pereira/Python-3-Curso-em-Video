# ex-013 Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

# Variáveis de entrada.
funcionario = input('Digite o nome do funcionário: ')
salario = float(input(f'digite o salário de {funcionario}: '))

# Variável de calculo de porentagem.
salarionovo = (salario + (salario * 15) /100)

print(f'O salário atual de {funcionario} é de {salario} R$, e com um aumento de 15% ficará em, {salarionovo} R$ . ')