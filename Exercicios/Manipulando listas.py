"""
Descrição
Ambrosiana tem um delivery de frango assado.

O seu problema atual é o gerenciamento da lista de pedidos.

Cada pedido corresponde a um número inteiro  (1 <= PEDIDO <= 10000).
Os pedidos podem ser cancelados a qualquer momento.
Além disso, de tempos em tempos, é importante ter a lista de pedidos atualizada em sua mesa.

Sua missão é ajudar no gerenciamento dos pedidos, considerando que novos pedidos podem ser adicionados
à lista assim como podem ser removidos. O programa deve encerrar quando a entrada for igual ao caracter s.

Formato de entrada

A entrada consiste de várias linhas, sendo que cada linha pode ser:

um novo pedido: nesse caso, a linha inicia com a letra a seguida do PEDIDO.
Significa que o PEDIDO deve ser adicionado na fila de pedidos.
cancelamento de um pedido: nesse caso, a linha inicia com a letra r  seguida do PEDIDO.
Significa que o PEDIDO deve ser removido da fila. Não existem PEDIDOS duplicados na fila.
Se o PEDIDO existir, você deve imprimir "removido", caso contrário imprima "falha".
impressão da lista de pedidos: nesse caso, a linha inicia com a letra p.
Significa que você deve imprimir a lista de pedidos. Nesse caso, imprima todos os números na mesma linha separados por espaços.
Depois do último número não existe espaço.
O programa deve parar quando for digitado o caracter s.

Formato de saída

A saída deve ser impressa de acordo com as entradas dadas.
"""

def SeparaValores(vlr):
    if len(vlr) == 1:
        for item in range(len(vlr)):
            comand = str(vlr[0])
            break
        return comand
    elif len(vlr) == 2:
        for item in range(len(vlr)):
            comand = str(vlr[0])
            values = int(vlr[1])
        return comand, values


def Valid_Pedido(v2):
    return v2 >= 1 and v2 <= 10000


def Valid_Comando(comand):
    valor1 = "s"
    return comand == valor1


def Verificacao(values):
    if len(values) == 1:
        comand = SeparaValores(values)
        if comand == "p":
            return comand
        while not Valid_Comando(comand):
            values = input().split()
            comand = SeparaValores(values)
        return comand
    elif len(values) == 2:
        comand, number = SeparaValores(values)
        while (not Valid_Comando(comand)) and (not Valid_Pedido(number)):
            values = input().split()
            comand, number = SeparaValores(values)
        return comand, number


lista_numerica = []

#Primeira Parte
valores = input().split()
qtd_valores = len(valores)

if qtd_valores == 1:
    comando = Verificacao(valores)

elif qtd_valores == 2:
    comando, numero = Verificacao(valores)


# Segunda parte
while comando != "s":
    if comando == "a":
        lista_numerica.append(numero)
        valores = input().split()
        if len(valores) == 1:
            comando = Verificacao(valores)
        elif len(valores) == 2:
            comando, numero = Verificacao(valores)

    elif comando == "r":
        if numero in lista_numerica:
            lista_numerica.remove(numero)
            print("removido")
        else:
            print("falha")
        valores = input().split()
        if len(valores) == 1:
            comando = Verificacao(valores)
        elif len(valores) == 2:
            comando, numero = Verificacao(valores)

    elif comando == "p":
        if lista_numerica == []:
            print("vazia")
        else:
            lista = str(lista_numerica).replace('[', '').replace("]", "").replace(",", "")
            print(lista)
        valores = input().split()
        if len(valores) == 1:
            comando = Verificacao(valores)
        elif len(valores) == 2:
            comando, numero = Verificacao(valores)