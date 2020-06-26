"""
Crie um programa que tenha uma única função, além da principal, que receberá como parâmetro um natural n (0<=n<=2^30) e devolverá a quantidade de dígitos de n. O programa exibirá o retorno da função. Observações: (a) apenas um laço de repetição; (b) sem matrizes; (c) função iterativa.

Formato de entrada

12345678

Formato de saída

8
"""

def achaTamanho(x):
    a = str(x)
    num = int(0)

    for caracter in a:
        if caracter in '0123456789':
            num = num + 1
    return(num)


num = int(input())
if num < 0 or num <= 1073741824:
    n = achaTamanho(num)
print(n)
