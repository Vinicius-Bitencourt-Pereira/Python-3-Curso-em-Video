'''
 Ex- 29 Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma
mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
'''
# Recebendo a velocidade atual do carro.
velocidade_atual = int(input('Em que velocidade voce esta? '))

# Velocidade limite da via: 80km/h
velocidade_limite = 80

# Multa p/ cada km acima de 80km/h: 7 R$
multa = 7.00

# Valor total da multa se a velocidade estiver acima do permitido.
multa_total = (velocidade_atual - velocidade_limite) * multa

# Verificando se a velocidade atual esta dentro do limite.
if velocidade_atual > velocidade_limite :
   print(f'ATENÇÃO!!! Você está acima da velocidade permitida que é de {velocidade_limite} KM/h. ')
   print(f'Você foi multado em {multa_total} R$.')
else:
  print('Siga com prudencia, Boa Viagem!.')
