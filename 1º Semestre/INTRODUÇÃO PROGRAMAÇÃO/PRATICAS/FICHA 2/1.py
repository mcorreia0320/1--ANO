#Escreva um programa em Python que aplique o Teorema de Pitágoras (h2=c2 + c2) para calcular a hipotenusa
#de um triângulo rectângulo a partir dos comprimentos dos dois catetos introduzidos pelo utilizador.
from math import sqrt
def calcular_hipotenusa(cateto1_input, cateto2_input):
    return sqrt ((cateto1_input**2) + (cateto2_input**2))

cateto1 = eval(input('Escreva o cateto 1:'))
cateto2 = eval(input('Escreva o cateto 2:'))

print('A hipotenusa é', calcular_hipotenusa(cateto1, cateto2))
    


