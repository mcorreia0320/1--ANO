#Escreva em Python a função duplica que recebe um tuplo e tem como valor um tuplo idêntico ao original,
#mas em que cada elemento está repetido. Por exemplo,
#>>> duplica((1,2,3))
#(1,1,2,2,3,3)


def duplica(tuplo):
    tuplo1=()
    for elemento in tuplo:
        tuplo1 += (elemento, elemento,)
    return tuplo1
        
        

    
t1= (1,2,3)

print(duplica(t1))