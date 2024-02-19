#Escreva a função cria_lista_multiplos que recebe um número inteiro positivo, e devolve uma lista
#com os dez primeiros múltiplos desse número. A sua função deve testar se o seu argumento é um número inteiro
#positivo e dar uma mensagem de erro adequada em caso contrário. Considere que zero é múltiplo de todos os
#números. Por exemplo, 
#>>> cria_lista_multiplos (6)
#[0, 6, 12, 18, 24, 30, 36, 42, 48, 54]

def cria_lista_multiplos(inteiro):
    if inteiro is not int and inteiro < 0:
        raise ValueError ('O numero indicado não é inteiro positivo')
    lista_vazia= []
    for multiplos in range(10):
        lista_vazia += ((inteiro *multiplos),)
    return lista_vazia
            
        