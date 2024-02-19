tuplo= (1,2,3,4,5)

def soma_elementos(tuplo):
    soma= 0
    indice= 0
    
   
    while indice < len(tuplo):
        
        soma+= tuplo[indice]
        indice+= 1
        
    return soma

print('soma dos elementos:', soma_elementos(tuplo))
        