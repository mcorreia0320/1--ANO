#Escreva uma função chamada posicoes_lista que recebe uma lista e um elemento, e devolve uma lista
#contendo todas as posições em que o elemento ocorre na lista. Por exemplo,
#>>> posicoes_lista (['a', 2, 'b', 'a'], 'a')
#[0, 3]

def posicoes_lista(lista, valor):
    lista_vazia= []
    for indice in range (len(lista)):
        if lista[indice] == valor:
            lista_vazia += [indice]
    return lista_vazia
            