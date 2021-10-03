# Ex- 049: Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

# Recebendo o numero do usuário.
numero = int(input('Digite um número que eu te devolvo sua tabuada: '))

# Imprimindo o número esolhido.
print(f'A tabuada de {numero} é: ')

# Loop de 1 a 10.
for x in range(1,11):
  # Imprimindo o resultado. Multiplicando na própria lina a cada loop.
  # x:2 é para deixar o resultado de forma alinhada.
  print(f'{x:2} x {numero} = { x * numero } ')
