"""
Descrição
Faça um programa em Python3 que receba um valor em polegadas, converta e imprima o resultado em milímetros.

Formato de entrada

A entrada será um número real e não deve ser impresso nenhum texto para pedi-la.

Formato de saída

A saída deverá ser formatada conforme o exemplo:

<valor1> polegada(s) eh o mesmo que <valor2> mm
Onde <valor1> deverá ser substituído pelo valor em polegadas e <valor2> pelo resultado em milímetros. Os números devem ser exibidos sem nenhuma formatação explícita quanto ao número de casas decimais.

OBS.: Atenção aos acentos no texto de saída.

o The Huxley não aceita caracteres acentuados mesmo nas strings
"""

p = float(input())

mm = p * 25.4

print(f'{p} polegada(s) eh o mesmo que {mm} mm')