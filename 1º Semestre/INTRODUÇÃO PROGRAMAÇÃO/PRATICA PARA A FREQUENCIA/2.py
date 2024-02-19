#1 Exercicio 

def operações():
    valor1 = eval(input('Escreva um valor: '))
    valor2 = eval(input('Escreva um valor: '))
    
    print('Soma: ',valor1 + valor2)
    print('Substração: ',valor1 - valor2)
    print('Multiplicação: ',valor1 * valor2)
    print('Divisão: ',valor1 / valor2)
    return

#2 Exercicio

def divisores(numero):
    divisor = 0
    indice = 1
    while indice <= numero:
        if numero % indice == 0:
            divisor += 1
        indice += 1
    return print('O número tem',divisor,'divisores')

#3 Exercicio

tuplo_inteiros= (1,-3, 5, 2)

def impares_positivos(tuplo):
    tuplo_vazio= ()
    for elementos in tuplo:
        if elementos % 2 != 0:
            if elementos > 0:
                tuplo_vazio += (elementos,)
    return tuplo_vazio

#4 Exercicio

lista_a_receber= ['a', 5, 0.1, 2, 1]

def menor_maior(lista_receber):
    lista_vazia= []
    maior= 0
    for elemento in lista_receber:
        if type(elemento) == int:
            if elemento > maior:
                maior = elemento
    
    menor = maior
    for elemento in lista_receber:
        if type(elemento) == int:
            if elemento < menor:
                menor = elemento
    lista_vazia=[menor, maior]
    return lista_vazia

#5 Exercicio

cadeia_caracteres= 'aabbc'

def conta_caracteres(texto):
    dicionario_vazia= {}
    for caracter in texto:
        if caracter not in dicionario_vazia:
            dicionario_vazia[caracter] = 1 
        else:
            dicionario_vazia[caracter] += 1
    return dicionario_vazia
        
    
            
            
        
    
    
        
        
    