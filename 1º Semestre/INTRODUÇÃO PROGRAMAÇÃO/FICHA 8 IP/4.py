#Crie duas funções, soma_quadrados_while que recorre ao ciclo while, e
#soma_quadrados_for, que recorre ao ciclo for, que recebem uma lista de inteiros e devolvem a
#soma dos quadrados dos elementos da lista.
#Por exemplo, soma_quadrados_while([1,2,3]) deverá retornar 14.

def soma_quadrados_while(lista_de_inteiros):
    resultado = 0
    indice = 0
    while indice < len(lista_de_inteiros):
        resultado += (lista_de_inteiros[indice])**2
        indice += 1
    return resultado

def soma_quadrados_for(lista_de_inteiros):
    resultado= 0
    for elementos in lista_de_inteiros:
        resultado += elementos ** 2
    return resultado