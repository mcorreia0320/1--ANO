#Utilizando a função area_circulo do exercício anterior, escreva uma função com o nome area_coroa
#que recebe dois argumentos, r1 e r2, e tem como valor a área da coroa circular de raio interior r1 e raio exterior
#r2. A sua função deverá gerar um erro de valor (ValueError) se o valor de r1 for maior que o valor de r2.

def area_circulo(raio_circulo):
    area = 3.14 * (raio_circulo**2)
    return area

def area_coroa(r1, r2):
    if r1 > r2:
        raise ValueError
    area_coroa= area_circulo(r2) - area_circulo(r1)
    return area_coroa


