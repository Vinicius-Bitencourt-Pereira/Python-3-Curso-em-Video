# A Função input()

#  A função input() faz uma pausa no programa e espera uma entrada do usuário pelo terminal. Para ler a entrada do usuário
# a função input() espera que após digitada a entrada o usuário aperte a tecla enter, após isso input()
# lê essa entrada como uma string, portanto, se a entrada esperada for um número ela deve ser convertida
# usando-se as funções de conversão int() ou float().

# ex-001 Escreva um programa que leia um nome e mostre uma mensagem de boas vindas.

#  Criando uma variável chamada 'nome' do tipo string, que recebe o input do usuário. Após digitado os dados, pressionado
# enter, aparece uma mensagem de boas vindas na tela.

nome = input(str('Qual seu nome ? '))
print ('Ola,', nome , 'seja muito bem vindo!')