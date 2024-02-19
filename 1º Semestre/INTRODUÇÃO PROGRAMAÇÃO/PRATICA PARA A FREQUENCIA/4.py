#EXERCICIO 1

def maior_ou_igual():
    
    valor1= eval(input('Introduza um valor: '))
    valor2= eval(input('Introduza outro valor: '))
    
    if valor1 > valor2:
        print('O valor maior é', valor1)
    
    elif valor1 < valor2:
        print('O valor maior é', valor2)
    
    elif valor1 == valor2:
        print('Os dois valores são iguais')
        
#EXERCICIO 2

def pares_impares(numero):
    
    pares = 0
    impares = 0
    
    while numero > 0:
        
        digito = numero % 10
        
        if digito % 2 == 0:
            pares += 1
        else:
            impares += 1
        
        numero = numero // 10
    
    print('Pares:',pares,'\nImpares:',impares)
    
#EXERCICIO 3

def pares(inteiro_positivo):
    tuplo_resultado= ()
    indice= 0
    
    while indice <= inteiro_positivo:
        tuplo_resultado += (indice,)
        indice += 2
    return tuplo_resultado

#EXERCICIO 4

dicionario = {'a':1, 'b':(1,2), 'c':"abc"}

def lista_valores(dicionario):
    
    lista_resultado = []
    
    for chave in dicionario:
        lista_resultado += [dicionario[chave]]
    
    return lista_resultado

#EXERCICIO 5

def divisores(inteiro):
    dicionario = {inteiro:[]}
    
    divisores= 1
    
    while divisores <= inteiro:
        
        if inteiro % divisores == 0:
            dicionario[inteiro] += [divisores]
        
        divisores += 1
    
    return dicionario

#EXERCICIO 6

def operações():
    
    valor1= eval(input('Introduza um valor: '))
    valor2= eval(input('Introduza outro valor: '))
    
    soma = valor1 + valor2
    substração = valor1 - valor2
    multiplicação = valor1 * valor2
    divisão = round(valor1 / valor2,3)
    
    print('Soma:',soma,'\nSubstração:',substração,'\nMultiplicação',multiplicação,'\nDivisão',divisão)
    
#EXERCICIO 7

def num_divisores(numero):
    divisores = 0
    
    indice= 1
    
    while indice <= numero:
        
        if numero % indice == 0:
            divisores += 1
        
        indice += 1
    
    return divisores

#EXERCICIO 8

tuplo_inteiros= (1,-3,5,2)

def impares_positivos(tuplo):
    tuplo_vazio = ()
    
    for elemento in tuplo:
        
        if elemento > 0:
            if type(elemento) == int:
                if elemento % 2 != 0:
                    tuplo_vazio += (elemento,)
    return tuplo_vazio

#EXERCICIO 9

lista_elementos = ['a',5,0.1,2,1]

def menor_maior(lista):
    lista_resultado = []
    
    maior = 0
    for elemento in lista:
        if type(elemento) == int:
            if maior < elemento:
                maior = elemento
    
    menor = maior
    for elemento in lista:
        if type(elemento) == int:
            if menor > elemento:
                menor = elemento    
            
    
    lista_resultado = [menor,maior]
    
    return lista_resultado

#EXERCICIO 10

def caracteres(texto):
    
    dicionario={}
    
    for caracter in texto:
        
        if caracter not in dicionario:
            dicionario[caracter] = 1
        
        else:
            dicionario[caracter] += 1
    
    return dicionario
            
                
            
            
            
            
            
    
    
    
        
        
    
    