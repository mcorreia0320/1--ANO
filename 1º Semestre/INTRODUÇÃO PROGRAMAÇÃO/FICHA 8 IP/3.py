#Escreva uma função triplica que recebe um tuplo e tem como valor o tuplo que se obtém do tuplo
#original, repetindo cada elemento três vezes.
#Por exemplo triplica((2,0)) deverá retornar (2,2,2,0,0,0).

def triplica(tuplo):
    tuplo_vazio= ()
    for elemento in tuplo:
        tuplo_vazio += (elemento, elemento, elemento,)
    return tuplo_vazio

print(triplica((2,0)))

