lista= ([1, 2, 3, 2, 4], 2, 'a')

def substitui_while(lista_recibida, velho, novo):
    indice = 0
    while indice < len(lista_recibida):
        if lista_recibida[indice] == velho:
            lista_recibida[indice] = novo
        indice += 1
    return lista_recibida

def substitui_enumerate(lista_recibida, velho, novo):
    for indice, elemento in enumerate(lista_recibida):
        if lista_recibida[indice] == velho:
            lista_recibida[indice] = novo
    return lista_recibida



    
    