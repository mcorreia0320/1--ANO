#Escreva uma função soma_quadrados_valores que soma os quadrados de todos os valores num
#dicionário.#Por exemplo, soma_quadrados_valores({'a':2, 'b':5, 'c':3}) deverá retornar 38.

def soma_quadrados_valores(dicionario):
    resultado= 0
    for chaves in dicionario:
            resultado += dicionario[chaves]**2
    return resultado