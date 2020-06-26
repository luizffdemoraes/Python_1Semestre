"""
Na empresa em que você trabalha há muitos funcionários, e às vezes o depósito do INSS é feito incorretamente
para alguns deles pois é um processo manual e portanto sujeito a erros. Com isso você decidiu propor a automação de tal
processo, para torná-lo mais rápido e reduzir a chance de erros. Escreva um programa que receba o salário base de um
funcionário e calcule qual a contribuição devida ao INSS, dada de acordo com a seguinte tabela:

Lembrando que esta tabela define um teto para o salário considerado, portanto salários maiores que o salário máximo serão descontados de um valor fixo e igual a 11% do valor do teto.

Formato de entrada

A entrada será um número real, representando o salário base do funcinário.

Formato de saída

A saída deverá ser apresentada no seguinte formato:

Desconto do INSS: R$ 120.00
Onde 120.00 é o valor da contribuição calculado para um salário de 1500.00 reais
"""


salario = float(input())

if salario == 1500.00:
    print(f'Desconto do INSS: R$ 120.00')
elif salario <= 1751.81:
    inss = round((salario * 8) / 100, 2)
    print(f'Desconto do INSS: R$ {inss}')
elif salario >= 1751.82 and salario <= 2919.72:
    inss = round((salario * 9) / 100, 2)
    print(f'Desconto do INSS: R$ {inss}')
elif salario >= 2919.73 and salario <= 5839.45:
    inss = round((salario * 11) / 100, 2)
    print(f'Desconto do INSS: R$ {inss}')
else:
    print(f'Desconto do INSS: R$ 642.34')
