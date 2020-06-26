"""
Descrição
Agora que o nosso caixa de autoatendimento é capaz de processar o pacote e calcular o preço da postagem, está faltando calcular a quantidade de selos que o usuário deve comprar para poder pagar pela postagem.

Sabemos que esta rede de agências de correios só trabalha com selos de 20 e 50 centavos, portanto devemos calcular qual a combinação de selos de 20 e 50 centavos dará o o valor EXATO do custo de postagem. Da primeira parte do exercício, podemos concluir que o custo do pacote deve respeitar:
custo mínimo de 70 centavos;
custo máximo de R$ 6.20; e
custo é sempre um múltiplo de 10 centavos.
Queremos também imprimir sempre a menor quantidade de selos possível, portanto se o custo total for R$ 2.00, queremos 4 selos de R$ 0.50, e não queremos 10 selos de R$ 0.20 nem 2 selos de R$ 0.50 mais 5 selos de R$ 0.20.
Escreva um programa que em reais e:
Verifique se o número recebido é um custo válido (deve respeitar as condições dadas acima)
Calcule a quantidade de selos de 50 e 20 centavos a serem compradas pelo usuário.
Dica 1: Para não ter problemas com arredondamento, converta o valor recebido para centavos antes de fazer qualquer verificação ou cálculo.

Dica 2: Para descobrir como calcular a quantidade de selos, pense sempre em pegar a maior quantidade possível de selos de 50 (análogo ao problema da tinta, mas agora não é permitido comprar selos a mais, o valor deve ser exato). Portanto faça uma tabela com os preços de 10 em 10 centavos, escreva para cada caso quantos selos são necessários e tente encontrar um padrão.
Por exemplo, a maior quantidade de selos de 50 para um custo de R$ 1,10 é 2, mas ai não conseguimos preencher os 10 centavos que faltam. Mas é possível chegar ao valor exato com um selo de 50 a menos e 3 selos de 20. Seguindo este exemplo, o que acontece com o valor de 1,60? e 2,10? 2,60? Qual a relação entre esses valores e o selo de 50?
Formato de entrada

A entrada será um número real representando o custo de postagem do pacote. (Caso haja entradas inválidas, elas serão separadas por uma quebra de linha e a última entrada é sempre válida)

Formato de saída

Enquanto o preço entrado for um valor inválido, o programa deve imprimir:
"Preco invalido, refaça a leitura do pacote."
Quando o preço entrado for válido, deve ser impressa a seguinte mensagem:
"Compre X selo(s) de R$ 0.50 e Y selo(s) de R$ 0.20!"
Onde X e Y são as quantidades calculadas para cada selo.
"""

custo = float(input())
t = round(custo * 100)
while custo < 0.70 or custo > 6.20 or t % 10 != 0:
    print('Preco invalido, refaca a leitura do pacote.')
    custo = float(input())
    t = round(custo * 100)


selo_50 = int(custo // 0.5)
resto_50 = round(custo - (selo_50 * 0.50), 2)
selo_20 = int(resto_50 // 0.2)

if resto_50 == 0.10:
    selos_50 = int(selo_50 - 1)
    s_50 = round(custo - (selos_50 * 0.50), 2)
    selo_20 = int(s_50 // 0.2) + 1
    print(f'Compre {selos_50} selo(s) de R$ 0.50 e {selo_20} selo(s) de R$ 0.20!')
elif resto_50 % 0.2 != 0:
    selos_50 = int(selo_50 - 1)
    s_50 = round(custo - ((selo_50 - 1) * 0.50), 2)
    selo_20 = int(s_50 // 0.2)
    print(f'Compre {selos_50} selo(s) de R$ 0.50 e {selo_20} selo(s) de R$ 0.20!')
else:
    print(f'Compre {selo_50} selo(s) de R$ 0.50 e {selo_20} selo(s) de R$ 0.20!')
