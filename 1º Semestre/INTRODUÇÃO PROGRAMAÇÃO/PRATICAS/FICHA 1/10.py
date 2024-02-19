#1 

Ano = eval(input('Escreva um ano para eu dizer se é bissexto \nAno ->'))

#2 condiçoes

if Ano % 4 == 0 and  Ano % 100 != 0:
    print('O ano', Ano, 'é bissexto')

elif Ano % 4 == 0 and Ano % 100 == 0 and Ano % 400 == 0:
    print('O ano', Ano, 'é bissexto')
    
else:
    print('O ano', Ano, 'não é bissexto')
    

    



