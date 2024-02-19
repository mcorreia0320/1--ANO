

def duplica(tuplo, repetições):
    tuplo1=()
    for elemento in tuplo:
        for _ in range (repetições):
            tuplo1 += (elemento,)
            
    return tuplo1
        
        

    
t1= (1,2,3)

print(duplica((t1),5))