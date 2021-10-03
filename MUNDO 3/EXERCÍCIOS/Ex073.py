'''
Ex 73 - Crie uma tupla preenchida com os 20 primeiros colocados da Tabela
do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:

a) Os 5 primeiros times.

b) Os últimos 4 colocados.

c) Times em ordem alfabética.

d) Em que posição está o time da Chapecoense.'''


times = ('ATLÉTICO-MG', 'PALMEIRAS', 'FLAMENGO', 'FORTALEZA EC', 'BRAGANTINO', 'CORINTHIANS',
         'FLUMINENSE', 'CUIABÁ', 'INTERNACIONAL', 'ATLÉTICO GOIANIENSE', 'ATHLETICO-PR',
         'CEARÁ', 'SANTOS', 'JUVENTUDE', 'BAHIA', 'SÃO PAULO', 'AMÉRICA-MG', 'GREMIO', 'SPORT',
         'CHAPECOENSE')

print('Imprimindo a  Classificação Brasileirão Série A')
print('==' * 36)
for x in times:
  print(x)
print('==' * 36)
print(f'- Os 5 primeiros colocados no brasileirão são:\n{times[:5]}')
print('==' * 36)
print(f'- Os 4 últimos colocados no brasileirão são:\n{times[-4:]}')
print('==' * 36)
print('impresão em ordem alfabética')
print('==' * 36)
ordem_alfabética = sorted(times)
for t in  ordem_alfabética:
  print(t)
print('==' * 36)
print(f'A chapecoense se encontra na {times.index("CHAPECOENSE") + 1}ª posição')
