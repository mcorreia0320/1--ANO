#Escreva a função agrupa_por_chave que dada uma lista de pares chave valor (k, v) (representados
#por tuplos de dois elementos) devolve um dicionário que a cada chave k associa uma lista com os valores v, para
#essa chave encontrados na lista passada como argumento. Por exemplo,
#>>> agrupa_por_chave ([('a', 8), ('b', 9), ('a', 3)])
#{'a': [8,3], 'b': [9]}

def agrupa_por_chave(lista):
    dicionario={}
    for elementos in lista:
        chave= elementos[0]
        valor= elementos[1]
        if chave not in dicionario:
            dicionario[chave] = [valor]
        else:
            dicionario[chave] += [valor]
    return dicionario