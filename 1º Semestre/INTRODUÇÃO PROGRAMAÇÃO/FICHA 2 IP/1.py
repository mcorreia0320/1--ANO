#Escreva um programa em Python que aplique o Teorema de Pitágoras (h2=c2 + c2) para calcular a hipotenusa
#de um triângulo rectângulo a partir dos comprimentos dos dois catetos introduzidos pelo utilizador. 

#1 

from math import sqrt

#2 

cateto1= eval(input('Escreva um valor: '))
cateto2= eval(input('Escreva outro valor: '))

#3 

h = ( (cateto1 ** 2) + (cateto2 ** 2) )

resultado = sqrt(h)

#4

print('O valor da hipotenusa é:', resultado)