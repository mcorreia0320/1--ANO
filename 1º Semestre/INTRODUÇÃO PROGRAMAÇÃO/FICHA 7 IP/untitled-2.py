#2. Uma carta de jogar é caracterizada por um naipe (espadas, copas, ouros e paus) e por um valor (A, 2, 3, 4, 5, 6,
#7, 8, 9, 10, J, Q, K). Uma carta pode ser representada por um dicionário com duas chaves, 'np', e 'vlr', sendo
#um conjunto de cartas representado por uma lista de cartas.

#a. Escreva uma função em Pyhton que devolve uma lista contendo todas as cartas de um baralho.

#b. Recorrendo à função random (), a qual produz um número aleatório no intervalo [0,1[, escreva a
#função baralha, que recebe uma lista correspondente a um baralho de cartas e baralha aleatoriamente
#essas cartas, devolvendo a lista que corresponde às cartas baralhadas. Sugestão: percorra
#sucessivamente as cartas do baralho trocando cada uma delas por uma outra carta selecionada
#aleatoriamente. 


from random import random
def baralho():
    lista_a_retornar= []
    for naipe in ['esp', 'copas', 'ouros', 'paus']:
        for valor in ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']:
            lista_a_retornar += [{'naipe':naipe, 'valor':valor}]
    return lista_a_retornar

lista= baralho()

def baralha(lista_a_baralhar):
    for indice_atual in range (len(lista_a_baralhar)):
        numero_aleatorio = int(random()*len(lista_a_baralhar))
        lista_a_baralhar[indice_atual], lista_a_baralhar[numero_aleatorio] =lista_a_baralhar[numero_aleatorio],lista_a_baralhar[indice_atual]
    return lista_a_baralhar