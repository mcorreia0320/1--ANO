#Utilizando a função area_circulo do exercício anterior, escreva uma função com o nome area_coroa
#que recebe dois argumentos, r1 e r2, e tem como valor a área da coroa circular de raio interior r1 e raio exterior
#r2. A sua função deverá gerar um erro de valor (ValueError) se o valor de r1 for maior que o valor de r2. 

def area_circulo (raio):
    area= 3.14 * (raio**2)
    return area

def area_coroa (r1, r2):
    if r1 > r2:
        raise ValueError
    
    else: 
        coroa = area_circulo (r2) - area_circulo (r1)
               
    return coroa

area_exterior= eval(input('Escreva raio exterior: '))
area_interior= eval(input('Escreva raio interior: '))

print('Area da Coroa é %0.1f' % (area_coroa (area_interior, area_exterior)))
#print('Area da Coroa é:', area_coroa (area_interior, area_exterior))
            


    