#1 EXERCICIO

def calcula_tempo(numero_segundos):
    
    dias= numero_segundos // 86400 #dias
    sobrante1= numero_segundos % 86400 #horas em segundos
    
    horas= sobrante1 // 3600 #horas
    sobrante2 = sobrante1 % 3600 #minutos em segundos
    
    minutos= sobrante2 // 60 #minutos
    sobrantes3= sobrante2 % 60 # segundos
    
    print('Dias:',dias,'\nHoras:',horas,'\nMinutos:',minutos,'\nSegundos:',sobrantes3)
    
#2 EXERCICIO

def entre_1_e_5():
    
    while True:
        
        inteiro = eval(input('Introduza um numero entre 1 e 5: '))
        
        if inteiro >= 1 and inteiro <= 5:
            print('\nO numero introduzido é ',inteiro)
            break
        
        else:
            print('\nNumero não aceite!')
            print('')
        
#3 EXERCICIO

def bissexto():
    
    ano = eval(input('Escreva um ano para eu dizer se é bissexto \nAno -> '))
    
    if ano % 4 == 0 and ano % 100 != 0 or ano % 4 == 0 and ano % 400 == 0:
        print('O ano',ano,'é bissexto')
    
    else:
        print('O ano',ano,'não é bissexto')
        
#4 EXERCICIO

def inteiro_impares():
    
    numero_impar= ''
    inteiro= eval(input('Escreva um inteiro \n? '))
    
    while inteiro > 0:
        
        digito= inteiro % 10 # Isolar digito
        
        if digito % 2 != 0: #Testa se é impar
            numero_impar += str(digito) #Guarda o digito
        
        inteiro = inteiro // 10 #Elimina o ultimo digito
    
    numero_impar_invertido = numero_impar[::-1]
    print('Resultado:', numero_impar_invertido)
    
#5 EXERCICIO

def contagem_15():
    
    control = 0
    numero = 0
    inteiro= eval(input('Insira um número entre 1 e 15: '))
    
    while numero <= 15:
        numero = inteiro + control
        if numero <= 15:
            print('n=',numero)
            control += 1
      
#6 EXERCICIO

def soma_contagem():
    somatorio = 0
    control = 0
    numero = 0
    inteiro= eval(input('Insira um número entre 1 e 15: '))
    
    while numero <= 15:
        numero = inteiro + control
        if numero <= 15:
            print('n=',numero)
            control += 1 
            somatorio += numero
    return print('O somatorio é',somatorio)

def media_somatorio():
    somatorio= 0
    controlo= 0
    while somatorio < 500:
        inteiro = eval(input('Introduza um valor menor que 100: '))
        if inteiro < 100:
            somatorio += inteiro
            controlo += 1
            print('\nValor do somatorio:',somatorio,'\n')
            if somatorio >= 500:
                print('')
                print('O somatorio é',somatorio,'\ne a media é',somatorio/controlo) 
                print('')
        
        else:
            print('')
            print('-------> O valor inserido é maior que 100 \n         Tente de Novo')
            print('')
  
#7 EXERCICIO 

def troco_notas_e_moedas():
    tuplo_moedas_notas=(50,20,10,5,2,1,0.50,0.20,0.10,0.05,0.02,0.01)
    valor_a_trocar= eval(input('Introduza o valor a trocar: '))
    
    for notas_e_moedas in tuplo_moedas_notas:
            devolve= 0
            
            while valor_a_trocar >= notas_e_moedas:
                devolve += 1
                valor_a_trocar -= notas_e_moedas
            
            if notas_e_moedas > 2:
                print('Devolve',devolve,'nota(s) de',notas_e_moedas)
            elif notas_e_moedas == 2 or notas_e_moedas == 1:
                print('Devolve',devolve,'moeda(s) de',notas_e_moedas,'€') 
            elif notas_e_moedas < 1:
                print('Devolve',devolve,'moedas(s) de',notas_e_moedas,'centimos')

#8 EXERCICIO

tuplo_algortimos = (2, 5, 6, 7, 9, 1, 8, 8)

def tuplo_pares(tuplo):
    tuplo_vazio= ()
    for elementos in tuplo:
        if elementos % 2 == 0:
            tuplo_vazio += (elementos,)
    return tuplo_vazio

#9 EXERCICIO 

tuplo_juntos=(1,2,2,3,3,4,4,5,5,6,6)

def juntos(tuplo):
    juntos = 0
    for indice in range(0, len(tuplo) -1, 1):
        if tuplo[indice] == tuplo[indice + 1]:
            juntos += 1
    return juntos
    
#10 EXERICIO

def num_divisores(inteiro):
    indice = 1
    quantidade_divisores = 0
    
    if inteiro == 0:
        return 0
    
    while indice <= inteiro:
        
        if inteiro % indice == 0:
            quantidade_divisores += 1
        indice += 1
    return quantidade_divisores

#11 EXERCICIO

tuplo_inteiros1= (2, 34, 200, 210)
tuplo_inteiros2=  (1, 23)

def junta_ordenados(tuplo1,tuplo2):
    
    indice1= 0
    indice2= 0
    
    tuplo_vazio = ()
    
    while indice1 < len(tuplo1) and indice2 < len(tuplo2):
        
        if tuplo1[indice1] < tuplo2[indice2]:
            tuplo_vazio += (tuplo1[indice1],)
            indice1 += 1
        
        else:
            tuplo_vazio += (tuplo2[indice2],)
            indice2 += 1
            
    tuplo_vazio += tuplo1[indice1:] + tuplo2[indice2:]
    return tuplo_vazio

#12 EXERCICIO

tuplo_inteiros3 = (3, 4, 5, 6, 7)

def conta_menores(tuplo, inteiro):
    controlo = 0
    for elemento in tuplo:
        if elemento < inteiro:
            controlo += 1
    return controlo
                
#13 EXERCICIO 

lista_numeros= [2, 3, 5, 9, 12, 33, 34, 45]
def remove_multiplos(lista, inteiro):
    lista_vazia= []
    
    for elementos in lista:
        if elementos % inteiro != 0:
            lista_vazia += [elementos]
    return lista_vazia
    
#14 EXERCICIO

lista_inteiros1= [2, 5, 90]
lista_inteiros2= [3, 5, 6, 12]

def junta_ordenadas_lista(lista1, lista2):
    lista_vazia= []
    indice1= 0
    indice2= 0
    
    while indice1 < len(lista1) and indice2 < len(lista2):
        
        if lista1[indice1] < lista2[indice2]:
            lista_vazia += [lista1[indice1]]
            indice1 += 1
        
        else:
            lista_vazia += [lista2[indice2]]
            indice2 += 1
            
    lista_vazia += lista1[indice1:] + lista2[indice2:]
    return lista_vazia

#15 EXERCICIO

lista1= ['a', ['b', 'c'], 5]

def duplica_elementos(lista):
    lista_vazia= []
    for elementos in lista:
        lista_vazia += [elementos, elementos]
    return lista_vazia

#16 EXERCICIO

def cria_lista_multiplos(inteiro):
    
    if type(inteiro) == int and inteiro > 0:
        lista_multiplos= [0]
        indice = 1
        while len(lista_multiplos) < 10:
            multiplo = inteiro * indice
            lista_multiplos += [multiplo]
            indice += 1
        
        return lista_multiplos
    
    else:
        print('')
        print('O valor indicado é incorreto \nPor favor, insita um valor inteiro positivo')
        
        
#17 EXERCICIO

def substitui(lista, velho, novo):
    for indice in range(0,len(lista),1):
        if lista[indice] == velho:
            lista[indice] = novo
    return lista

#18 EXERCICIO

def remove_repetidos(lista):
    lista_nova= []
    for elemento in lista:
        if elemento not in lista_nova:
            lista_nova += [elemento]
    return lista_nova
        
#19 EXERCICIO

def posicoes_lista(lista, elemento):
    lista_nova =[]
    for indice in range(0,len(lista),1):
        if lista[indice] == elemento:
            lista_nova += [indice]
    return lista_nova
    
#20 EXERCICIO

lista= [('a', 8), ('b', 9), ('a', 3)]

def agrupa_por_chave(lista):
    dicionario_vazio= {}
    
    for elemento in lista:
        chave = elemento[0]
        valor = elemento[1]
        
        if chave not in dicionario_vazio:
            dicionario_vazio[chave] = [valor]
        
        else:
            dicionario_vazio[chave] += [valor]
    
    return dicionario_vazio
            
#21 EXERCICIO

def numero1_20():
    
    numero= eval(input('Introduza um valor entre um e vinte: '))
    
    if numero <= 20 and numero >= 1:
        print('Número Aceite')
    
    else:
        print('Número Invalido')

#22 EXERCICIO

def existe_algarismo(numero, algarismo):
    
    valor_logico = False
    
    while numero > 0:
        
        digito = numero % 10
        
        if digito == algarismo:
            valor_logico = True
        
        numero = numero // 10
    
    if valor_logico == True:
        return True
    
    else:
        return False
    
#23 EXERCICIO 

def triplica(tuplo):
    tuplo_vazio = ()
    for elemento in tuplo:
        tuplo_vazio += (elemento, elemento, elemento)
    return tuplo_vazio
        
#24 EXERCICIO

def soma_quadrados_while(lista):
    somatorio = 0
    indice = 0
    
    while indice < len(lista):
        somatorio += (lista[indice])**2
        indice += 1
    
    return print('A soma dos quadrados dos elementos é',somatorio)

def soma_quadrados_for(lista):
    somatorio = 0
    
    for indice in range(0,len(lista),1):
        somatorio += (lista[indice])**2
    
    return print('A soma dos quadrados dos elementos é',somatorio)
    
#25 EXERCICIO

def soma_quadrados_valores(dicionario):
    somatorio= 0
    
    for chave in dicionario:
        somatorio += (dicionario[chave])**2
    
    return print('A soma dos quadrados dos elementos é',somatorio)
        
        
        
        
        
        
        
        
        
    
        