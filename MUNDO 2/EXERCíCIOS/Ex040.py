'''
# Ex- 40 Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
- Média abaixo de 5.0: REPROVADO
- Média entre 5.0 e 6.9: RECUPERAÇÃO
- Média 7.0 ou superior: APROVADO
'''
#  Recebendo as 2 notas e armazenando a média em media.
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2

# Comparando a média e imprimindo o resultado.
if media < 5.0:
    print(f'Sua média é: {media}')
    print(f'- Média abaixo de 5.0: REPROVADO')
elif media == 5.0 or media < 7:
    print(f'Sua média é: {media}')
    print(f'- Média entre 5.0 e 6.9: RECUPERAÇÃO')
else:
    print(f'Sua média é: {media}')
    print('- Média 7.0 ou superior: APROVADO')
