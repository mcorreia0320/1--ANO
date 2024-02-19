#Um número inteiro, n, diz-se triangular se existir um inteiro m tal que n = 1 +2 + ...+ (m-1)+ m. Escreva uma função
#chamada triangular que recebe um número inteiro positivo n, e cujo valor é True apenas se o número
#for triangular. No caso de n ser 0 deverá devolver False. Por exemplo,
#>>> triangular(6)
#True
#>>> triangular (8)
#False

def triangular(n):
    resultado= False
    formula= n*(n+1)/2
    if formula == 0:
        resultado= False
    else:
        resultado= True
        return resultado
        
    
