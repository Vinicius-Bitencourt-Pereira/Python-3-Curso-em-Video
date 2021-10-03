'''
# Ex- 43 Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
- IMC abaixo de 18,5: Abaixo do Peso
- Entre 18,5 e 25: Peso Ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade Mórbida
'''

# Recebendo o peso e a altura do usuário.
peso = float(input('Qual seu peso? (Kg)'))
altura = float(input('Qual sua altura? (M) '))

# Calculando o IMC.
imc = peso / (altura * altura)
# Imprimindo o IMC.
print(f'Resultado IMC: {imc:.2F}')

# Comparando o valor do IMC e imprimindo a categoria que a pessoa se encontra.
if imc < 18.5 :
  print('Esta pessoa está ABAIXO do peso!')
elif 18.5 <= imc < 25 :
  print('esta pessoa está com o peso IDEAL!')
elif 25 <= imc < 30 :
  print('esta pessoa está com SOBREPESO!')
elif 30 <= imc < 40 :
  print('esta pessoa está com o OBESIDADE!')
else:
  print('esta pessoa está com o OBESIDADE MÓRBIDA!')

