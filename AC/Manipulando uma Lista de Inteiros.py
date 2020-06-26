"""
Descrição
Escreva um programa que permita manipular uma lista de inteiros. Inicialmente o programa deve ler os inteiros separados por espaço em branco e armazenar em uma lista. Dado que os valores inteiros estão armazenados, o programa deve aceitar 4 comandos: inserir, remover, parcial e final. O comando inserir é acompanhado na mesma linha do valor inteiro a ser inserido na lista. Da mesma forma, o comando remover é acompanhado do valor a ser removido da lista. Já o comando parcial deve fazer com que os dados contidos na lista sejam impressos na tela, separados por espaços em branco e dispostos em ordem crescente(numérica). O mesmo deve fazer o comando final, exceto que este encerra a execução do programa.

Formato de entrada

Lista de valores inteiros separados por um espaço em branco na primeira linha.

Nas linhas seguintes, há 4 possíveis comandos: inserir, remover, parcial e final. Cada um destes ocupa uma linha. No caso dos comandos inserir e remover, é informado um valor inteiro.

Formato de saída

Linhas contendo os valores inteiros dispostos em ordem crescente (numérica) e separados por um espaço em branco.
"""

# Primeira PARTE
def ValidarNumInteiro(lista_num):
        for item in range(len(lista_num)):
            if lista_num[item].isnumeric():
                numeroI = lista_num[item]
                lista_num.append(int(numeroI))
            return(lista_num)


# Segunda PARTE
def SeparaTextoNumero(t, n):
    # Separar comando e valor
    for item in range(n):
        comand = str(t[0])
        number = int(t[1])
    return comand, number


# PRIMEIRA PARTE
lista = []
lista_numero = []
respI = "inserir"
respF = "final"
respR = "remover"
respP = "parcial"

# Primeira Parte
# Primeira lista numerica
lista = input().split()
numero = len(lista)

for item in range(len(lista)):
    if lista[item].isnumeric():
        numeroI = lista[item]
        lista_numero.append(int(numeroI))

while lista_numero is None or lista_numero == []:
    lista = input().split()
    lista_numero = ValidarNumInteiro(lista_numero)



# Segunda Parte
# Inserir informação
texto = input().split(' ')
n = len(texto)

# Condição para separar numero e texto
if n == 2:
    texto, numero = SeparaTextoNumero(texto, n)
else:
    for item in range(n):
        texto = str(texto[0])

while not (texto == respF):
    if texto == respI:
        lista_numero.insert(0, numero)
        # Inserir informação
        texto = input().split(" ")
        n = len(texto)

        # Condição para separar numero e texto
        if n == 2:
            texto, numero = SeparaTextoNumero(texto, n)
        else:
            for item in range(n):
                texto = str(texto[0])
    elif texto == respR:
        # Remover Número
        lista_numero.remove(numero)
        # Inserir informação
        texto = input().split(" ")
        n = len(texto)

        # Condição para separar numero e texto
        if n == 2:
            texto, numero = SeparaTextoNumero(texto, n)
        else:
            for item in range(n):
                texto = str(texto[0])
    elif texto == respP:
        lista = str(sorted(lista_numero)).replace('[', '').replace("]", "").replace(",", "")
        print(lista)

        # Inserir comandos
        texto = input().split(" ")
        n = len(texto)

        # Condi��o para separar numero e texto
        if n == 2:
            texto, numero = SeparaTextoNumero(texto, n)
        else:
            for item in range(n):
                texto = str(texto[0])

# Exibição
lista = str(sorted(lista_numero)).replace('[', '').replace("]", "").replace(",", "")
print(lista)