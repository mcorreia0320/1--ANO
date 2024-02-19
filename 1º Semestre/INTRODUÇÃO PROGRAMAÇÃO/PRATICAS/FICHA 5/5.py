#Escreva uma função em Python, com o nome conta_menores que recebe um tuplo contendo números inteiros e um
#número inteiro e que devolve o número de elementos do tuplo que são menores do que esse inteiro. Por exemplo,
#>>> conta_menores((3, 4, 5, 6, 7) , 5)
#2
#>>> conta_menores((3, 4, 5, 6, 7) , 2)
#0

def conta_menores(tuplo, inteiro):
    tuplo_vazio= ()
    controlo= 0
    for elementos in tuplo:
        if elementos < inteiro:
            controlo += 1
    return controlo