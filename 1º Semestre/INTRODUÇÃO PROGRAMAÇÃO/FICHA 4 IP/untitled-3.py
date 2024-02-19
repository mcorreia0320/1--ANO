def posições_lista (lista, elemento):
    lista_vazia= []
    for indice in range (0,len(lista)):
        if lista[indice] == elemento:
            lista_vazia += [indice]
    return lista_vazia


