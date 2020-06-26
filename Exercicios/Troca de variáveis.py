"""
Descrição
Complete o código do programa em Python3 que recebe dois valores quaisquer, armazenando-os nas variáveis v1 e v2, e em seguida troca os valores de v1 e v2 e imprime os valores trocados.

Formato de entrada

As entradas poderão ser quaisquer caracteres ou conjuntos de caracteres do teclado.

Formato de saída

A saída devera ser as duas entradas impressas na ordem inversa. Serão impressos os valores armazenados em v1 e v2, nessa ordem, mas o programa deverá ter trocado os valores recebidos em cada variável. (o valor originalmente em v1 passa para v2 e vice-versa).
"""

# O codigo para a entrada de dados e impressao
# dos resultados eh dado.
v1 = input()
v2 = input()

# insira na janela abaixo o codigo responsavel por
# trocar os valores de uma variavel para a outra
v1, v2 = v2, v1

print('valor em v1:', v1)
print('valor em v2:', v2)