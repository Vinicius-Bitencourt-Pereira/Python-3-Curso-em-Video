'''
Ex- 46: Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de
10 até 0, com uma pausa de 1 segundo entre eles.
'''

#  Fazer no pycharm, jogar o arquivo 'fogos.mp3' dentro da pasta do seu projeto,
# e add a variável path do diretório ao pycharm, para que o arquivo de audio
# seja descoerto pelo playsound.

# Importando a função ' sleep() ', do módulo ' TIME '.
from time import sleep

# Importando a função ' playsound() ', do módulo ' playsound '.
from playsound import playsound

# Criando um loop de contagem regressiva com o Loop 'FOR' de 10 até 0 (10, -1, -1).
for contagem in range(10, -1, -1):
    # Imprimindo 'contagem' com um delay de 1 segundo à cada loop.
    print(contagem)
    sleep(1)

# Imprimindo uma mensagem de 'FELIZ ANO NOVO!!!' NO FIM DO LOOP.
print(f'FELIZ ANO NOVO!!!')
# Tocando um som de queima de fogos de artifícil.
playsound('fogos.mp3')


