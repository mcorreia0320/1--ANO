#1 Exercicio
def maior(): #Função que retorna o maior
        
        valor1= eval(input('Escreva um valor: ')) #Pede ao utilizador para introduzir um valor
        valor2= eval(input('Escreva outro valor: ')) #Pede ao utilizador para introduzir um valor
        
        if valor1 > valor2: #Verefica qual é maior
                print('O maior é', valor1)
        else:
                print('O maior é', valor2)
        return

#2 Exercicio

def pares_impares(numero): #Função que retorna pares e impares
        pares= 0 #Pares
        impares= 0 #Impares
        while numero > 0: #Ciclo que acaba quando o numero for menor que 0
                digito = numero % 10 #Isola ultimo numero do digito
                if digito % 2 == 0: # Verifica se é par 
                        pares+= 1
                else: #Caso seja impar
                        impares+= 1
                numero = numero // 10 #Elimina o ultimo digito
        print(pares,'Pares e',impares,'Impares') 
        
#3 Exercicio 

def tuplo_com_pares(numero): #retorna tuplo com pares de 0 até o numero indicado
        tuplo_vazio= () #Tuplo a retonar
        if numero > 0: #Se o numero for positivo
                indice = 0 #Indice do ciclo
                while indice <= numero: #Ciclo que acaba quando o indice for maior ou igual que o numero
                        tuplo_vazio += (indice,) #Soma o valor ao tuplo
                        indice += 2 
        return tuplo_vazio

#4 Exercicio 

dicionario1 = {'a':1, 'b':(1,2), 'c':"abc"}

def chaves_dos_dicionarios(dicionario): #Funçao que retorna os valores das chaves dos dicionaerios
        lista_vazia = [] #Lista a retornar
        for chave in dicionario: #Percorre o dicionario
                lista_vazia += (dicionario[chave],) #Soma os valores de cada chave
        return lista_vazia

#5 Exercicio 

def divisores(inteiro): # Funcão que retorna divisores do inteiro dentro de un dicionario
        dicionario = {inteiro:[]} # dicionario a retornar
        indice= 1 #Indice do ciclo
        while indice <= inteiro: #Ciclo que acaba quando o  indice for menor ou igual a o inteiro
                if inteiro % indice == 0: #Verifica se o indice é divisor do inteiro
                        dicionario[inteiro] += [indice] #Soma o indice a chave do dicionario
                indice += 1
        return dicionario
                        


        


