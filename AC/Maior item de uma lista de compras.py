"""
Descrição
Dada uma lista de compras, queremos saber qual é o item mais caro da lista.

Formato de entrada

Uma sequência de itens, cada um descrito numa linha. Cada item contém um código de produto (um número inteiro), a quantidade do produto e o preço unitário (um float).

A sequência termina com um item com 0 como código do produto. Este último item não deve ser considerado para o cálculo.

Formato de saída

O código do produto, a quantidade e o preço do item mais caro, escrito com duas casas decimais.

Se a sequência não tiver itens deve se escrever "nao tem compras".

Se houver mais de um item com preço total mais caro, deverão ser impressos os dados do primeiro deles na lista de compras.
"""

def Valid(c, q, p):
    return 0 in c and 0 in q and 0 in p


codigo_lista = []
quantidade_lista = []
preco_lista = []
soma_lista = []
soma_listaStr = []
# contador de soma

lista = input().split()
codigo_lista.append(int(lista[0]))
quantidade_lista.append(int(lista[1]))
preco_lista.append(float(lista[2]))

while not (Valid(codigo_lista, quantidade_lista, preco_lista)):
    lista = input().split()
    codigo_lista.append(int(lista[0]))
    quantidade_lista.append(int(lista[1]))
    preco_lista.append(float(lista[2]))

    numero = len(codigo_lista)
    for item in range(numero):

        soma = float(quantidade_lista[item] * preco_lista[item])
        soma_lista.append(float(soma))


if sum(soma_lista) == 0:
    print('nao tem compras')
else:
    maior = float(max(soma_lista, key=float))
    indice = soma_lista.index(maior)
    print("Item mais caro")
    print(f"Codigo: {codigo_lista[indice]}")
    print(f"Quantidade: {quantidade_lista[indice]}")
    print(f'Custo: {maior:.2f}')
