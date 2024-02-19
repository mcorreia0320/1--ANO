#Escreva uma função chamada substitui que recebe uma lista, lst, dois valores, velho e novo, e
#devolve a lista que resulta de substituir em lst todas as ocorrências de velho por novo. Por exemplo,
#>>> substitui ([1, 2, 3, 2, 4], 2, 'a')
#[1, 'a', 3, 'a', 4]

def substitui(lista, velho, novo):
    lista_vazia=[]
    for e in lista:
        if e == velho:
            lista_vazia += [novo]
        else:
            lista_vazia += [e]
    return lista_vazia

def substitui_lista_recibida(lista_recibida, velho, novo):
    for indice in range (len(lista_recibida)):
        if lista_recibida[indice] == velho:
            lista_recibida[indice] = novo
    return lista_recibida