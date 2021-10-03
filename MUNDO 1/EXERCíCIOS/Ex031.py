'''
Ex-31 Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem,
 cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
'''
# Recebendo a distância da viagem em km.
distancia = float(input('Qual a distância da sua viagem em km? '))

# Para distâncias longas, R$ 0.45
distancia_longa = distancia * 0.45

# Para distância curta, R$ 0.50
distancia_curta = distancia * 0.50

# Comparando a distância e imprimindo o resultado após.
if distancia <= 200:
  print(f'O valo de sua passagem será {distancia_curta:.2f} R$.')
else :
  print(f'O valor de sua passagem será {distancia_longa:.2f} R$')
