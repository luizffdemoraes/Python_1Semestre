"""
Descrição
Faça um programa em Python3 que receba uma temperatura em Fahrenheit, calcule e imprima o valor convertido para a escala Celsius e para a escala Kelvin, de acordo com as equações de conversão abaixo:

t_celsius = (t_fahrenheit - 32) * 5/9

t_kelvin = t_celsius + 273.15
Formato de entrada

A entrada será um número real n, com n >= -459.67. (o zero absoluto, ou 0K, é igual a -459.67°F)

Formato de saída

A saída deverá ser formatada conforme o exemplo abaixo:

Convertendo <valor1>°F temos:
<valor2>°C e <valor3>K
Onde valor 1, 2 e 3 são respectivamente os valores de temperatura em Fahrenheit, Celsius e Kelvin.

Dica: para fazer o símbolo de grau, em um teclado PT, pode-se digitar AltGr + E. (AltGr é o Alt à direita da barra de espaço).

O caractere gerado com a combinação Alt + 167 é diferente do utilizado aqui e resultará em erro de comparação na resposta, se o seu teclado não tem esse caractere, você pode adicionar o teclado PT-BR (ABNT ou ABNT2) ou então copiar o símbolo do texto do enunciado.

Notem também que a temperatura Kelvin não leva o símbolo de grau. (Diz-se 250 Kelvin e não 250 graus Kelvin)
"""

t_fahrenheit = float(input())

t_celsius = (t_fahrenheit - 32) * 5/9

t_kelvin = t_celsius + 273.15


print(f'Convertendo {t_fahrenheit} °F temos:')
print(f'{t_celsius} °C e {t_kelvin} K')
