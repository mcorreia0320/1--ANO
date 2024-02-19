#Escreva uma função em Pyhton que recebe um dicionário cujos valores associados às chaves correspondem a
#lista de inteiros e que devolve o dicionário que se obtém "invertendo" o dicionário recebido no qual as chaves são
#os inteiros que correspondem aos valores do dicionário original e os valores são as chaves do dicionário original
#às quais os valores estão associados.

def inverter_dicionario(dicionario):
    dicionario_invertido= {}
    for chave in dicionario:
        for valores_das_chaves_dicionario in dicionario[chave]:
            if valores_das_chaves_dicionario not in dicionario_invertido:
                dicionario_invertido[valores_das_chaves_dicionario] = [chave]
            else:
                dicionario_invertido[valores_das_chaves_dicionario] += [chave]
    return dicionario_invertido

print(inverter_dicionario(inverter_dicionario({'a':[1,2], 'b':[1], 'c':[3], 'd':[4]})))
print(inverter_dicionario({'a':[1,2], 'b':[1], 'c':[3], 'd':[4]}))


def imprimir_dicionario(dicionario):
    for chave in dicionario:
        print(chave, ":", dicionario[chave])
        
        
print(imprimir_dicionario({'a':[1,2], 'b':[1], 'c':[3], 'd':[4]}))
            
            