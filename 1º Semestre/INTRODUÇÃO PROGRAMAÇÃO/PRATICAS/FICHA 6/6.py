#Escreva uma função com o nome remove_repetidos que recebe uma lista e devolve a lista obtida da lista
#original em que todos os elementos repetidos foram removidos. Por exemplo,
#>>> remove_repetidos ([2, 4, 3, 2, 2, 2, 3])
#[2, 4, 3]
#>>> remove_repetidos ([2, 5, 7])
#[2, 5, 7]

def remove_repetidos(lista):
    lista_vazia= []
    for elementos in lista:
        if elementos not in lista_vazia:
            lista_vazia += [elementos]
    return lista_vazia