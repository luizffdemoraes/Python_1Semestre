"""
Descrição
Escreva um programa que leia dois valores inteiros da entrada padrão e informe qual é o maior. Se os números forem iguais, imprima qualquer um deles.

Formato de entrada

Dois valores inteiros.

Formato de saída

O maior dentre os 2 valores fornecidos.
"""

num1 = int(input())
num2 = int(input())

if num1 > num2:
    print(num1)
elif num1 < num2:
    print(num2)
else:
    print(num1)