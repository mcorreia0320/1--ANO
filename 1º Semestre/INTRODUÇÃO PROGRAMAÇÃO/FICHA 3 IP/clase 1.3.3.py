t=(1,2,3,4,5)



def media_maior(tuplo):
        elemento = 0
        maior = tuplo[0]        
        valor= tuplo[0]
        for elemento in range (0, len(tuplo), 1):
                elemento += tuplo[elemento]
    
                if tuplo[elemento] > valor:
                        valor= tuplo[elemento]
        
        return (soma/len(tuplo), maior)        

print(media_maior(t))