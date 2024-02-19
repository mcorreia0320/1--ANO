#Escreva em Pyhton a função filtra_pares que recebe um tuplo contendo algarismos, verificando a
#correção do seu argumento, e devolve o tuplo contendo apenas os algarismos pares. Por exemplo,
#>>> filtra_pares((2, 5, 6, 7, 9, 1, 8, 8))
#(2, 6, 8, 8)

#1

def filtra_pares(tuplo):
    pares=()
    for elemento in tuplo:
        if elemento % 2 == 0:
            pares += (elemento,)
    return pares
    
t1= (3,2,1,4,65,0,8,1,2,10)

print(filtra_pares(t1))