"""
Descrição
Crie um programa que tenha uma única função, além da principal, que receberá como parâmetro um natural n (0<=n<=2^30) e devolverá a soma dos dígitos de n. O programa exibirá o retorno da função. Observações: (a) apenas um laço de repetição; (b) sem matrizes; (c) função iterativa.

Formato de entrada

12345678

Formato de saída

36
"""

def Fatiamento(n):
    lista = []
    texto = str(n)
    quantidade = len(texto)
    total = list(texto)
    for item in range(quantidade):
        x = int(total[item])
        lista.append(x)
    soma = sum(lista)
    print(soma)



numero = int(input())
if numero > 0 or numero <= 1073741824:
    Fatiamento(numero)
