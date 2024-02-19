#Escreva em Python a função duplica que recebe um tuplo e tem como valor um tuplo idêntico ao original,
#mas em que cada elemento está repetido. Por exemplo,
#>>> duplica((1,2,3))
#(1,1,2,2,3,3)

def duplica(tuplo):
    tuplo_duplicado= ()
    for elementos in tuplo:
        tuplo_duplicado += (elementos, elementos,)
    return tuplo_duplicado