# ex-014 Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

celsius = float(input('Digite a temperatura em graus celsius: '))
fahrenheit = (celsius * 1.8) + 32
print(f'A temperatuda de {celsius} °C graus celsius, em fahrenheit fica {fahrenheit:.1f} °F graus.')