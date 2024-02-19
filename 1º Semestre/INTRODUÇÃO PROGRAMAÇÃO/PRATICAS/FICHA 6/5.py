#Escreva uma função chamada substitui que recebe uma lista, lst, dois valores, velho e novo, e
#devolve a lista que resulta de substituir em lst todas as ocorrências de velho por novo. Por exemplo,
#>>> substitui ([1, 2, 3, 2, 4], 2, 'a')
#[1, 'a', 3, 'a', 4]

def substitui(lista, velho, novo):
    lista_a_retornar=[]
    for elemento in lista:
        if elemento == velho:
            lista_a_retornar += [novo]
        else:
            lista_a_retornar += [elemento]
    return lista_a_retornar

def substitui_range(lista, velho, novo):
    for indice in range(len(lista)):
        if lista[indice] == velho:
            lista[indice] = [novo]
    return lista