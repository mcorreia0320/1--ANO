#Defina uma função com o nome area_circulo que recebe o valor do raio de um círculo e tem como valor a
#área do círculo. Note-se que a área do círculo cujo raio 𝑟 é dada por 𝜋𝑟2. Use o valor 3.14 para o valor de 𝜋.
#def area_circulo (r1):
#area= 3.14 * (r1*r1)
#return area

#1 

def area_circulo (r1):
    area= 3.14 * (r1**2)
    return area


r1= eval(input('Escreva o raio: '))


print('A area do circulo é:', area_circulo(r1))

