t= (1,2,3,4,5)

def media_tuplo(tuplo):
    soma= 0
    for elementos in range(0,len(tuplo),1):
        soma += tuplo[elementos]
        
    return soma / len(tuplo)

print('media do tuplo', media_tuplo(t))