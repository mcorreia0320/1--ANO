#Escreva um programa em Python que aplique o Teorema de Pitágoras (h2=c2 + c2) para calcular a hipotenusa
#de um triângulo rectângulo a partir dos comprimentos dos dois catetos introduzidos pelo utilizador. 

#1 

from math import sqrt
def calcula_hipotenusa(cateto1_input, cateto2_input):
    #Funçao que calcula a hipotenusa usando o teorema de pitagoras#
    #Input: dois catetos#
    #Output: valor da hipotenusa#
    return sqrt ((cateto1_input**2)+(cateto2_input**2))

#2 

cateto1= eval(input('Escreva um valor: '))
cateto2= eval(input('Escreva outro valor: '))

cateto3= eval(input('Escreva um valor: '))
cateto4= eval(input('Escreva outro valor: '))

#3

print('O valor da hipotenusa é:', calcula_hipotenusa(cateto1, cateto2))



print('O valor da hipotenusa é:', calcula_hipotenusa(cateto3, cateto4))