def conta_palavras(texto_a_analisar):
    resultado={}
    indice_atual= 0
    while indice_atual < len(texto_a_analisar):
        #encontrar palavra
        inicio_palavra= indice_atual
        while indice_atual < len(texto_a_analisar) and texto_a_analisar[indice_atual] != '  ':
            indice_atual += 1
        palavra = texto_a_analisar[inicio_palavra:indice_atual]
        #adiciona palavra ao dicionario
        if palavra not in resultado:
            resultado[palavra] = 1
        else:
            resultado[palavra] += 1
        #INICIA a proxima palavra
        indice_atual += 1
    return resultado

def imrpime_dicionario(dicionario):
    total_de_palavras: 0
    for chave in dicionario:
        print(chave, ":", dicionario[chave])
        total_de_palavras += dicionario[chave]
    print('O total de palavras é:', total_de_palavras)
    
imrpime_dicionario(conta_palavras("Ola tudo  bem Ola"))