#Escreva uma função chamada posicoes_lista que recebe uma lista e um elemento, e devolve uma lista
#contendo todas as posições em que o elemento ocorre na lista. Por exemplo,
#>>> posicoes_lista (['a', 2, 'b', 'a'], 'a')
#[0, 3]

def posicoes_lista(lista, elemento):
    posições= []
    for indice in range(0, len(lista), 1):
        if lista[indice] == elemento:
            posições += [indice]
    return posições

