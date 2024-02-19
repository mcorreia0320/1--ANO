#Escreva em Pyhton a função filtra_pares que recebe um tuplo contendo algarismos, verificando a
#correção do seu argumento, e devolve o tuplo contendo apenas os algarismos pares. Por exemplo,
#>>> filtra_pares((2, 5, 6, 7, 9, 1, 8, 8))
#(2, 6, 8, 8)

def filtra_pares(tuplo):
    tuplo_vazio= ()
    for elementos in tuplo:
        if elementos % 2 == 0:
            tuplo_vazio += (elementos,)
    return tuplo_vazio
    