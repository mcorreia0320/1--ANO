tuplo= (1,2,3,4,5)


def media_tuplo(tuplo):
    soma= 0
    elemento= 0    
    
    while elemento < len(tuplo):
        soma+= tuplo[elemento]
        elemento+= 1
    
    return soma / len(tuplo)

print(media_tuplo(tuplo))
    