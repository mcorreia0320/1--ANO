#Escreva uma função com o nome remove_repetidos que recebe uma lista e devolve a lista obtida da lista
#original em que todos os elementos repetidos foram removidos. Por exemplo,
#>>> remove_repetidos ([2, 4, 3, 2, 2, 2, 3])
#[2, 4, 3]
#>>> remove_repetidos ([2, 5, 7])
#[2, 5, 7]
def remove_repetidos(lista):
    lista_nova= []
    for elemento in lista:
        if elemento not in lista_nova:
            lista_nova += [elemento]
    return lista_nova
        
        