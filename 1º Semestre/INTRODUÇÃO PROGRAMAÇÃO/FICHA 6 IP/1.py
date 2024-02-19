#1. Escreva a função remove_multiplos que recebe uma lista de números e um número e que devolve a lista
#original em que todos os múltiplos do segundo argumento são removidos. Por exemplo,
#>>> remove_multiplos ( [ 2, 3, 5, 9, 12, 33, 34, 45], 3)
#[2, 5, 34]

def remove_multiplos(lista, inteiro):
    lista_vazia=[]
    for e in lista:
        if e % inteiro != 0:
            lista_vazia += [e]
    return lista_vazia


lista1= [2,3,5,9,12,33,34,45]
inteiro1= 3

print(remove_multiplos(lista1, inteiro1))