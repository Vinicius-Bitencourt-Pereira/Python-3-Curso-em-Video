
# Ex- 57.1 Versão do professor!

# Receendo o sexo do usuário.
sexo = str(input('Digite o sexo do usuário [M/F]: ')).strip().upper()[0]
# Validando o valor de sexo. Enquanto nao for M m F ou f o loop pedirá a validação.
while sexo not in 'MmFm':
    # Imprime uma mensagem de opção inválida.
    sexo = str(input('Digite uma opção válida. insira M ou F: ')).strip().upper()[0]
print(f'Sexo {sexo} registrado com sucesso!')