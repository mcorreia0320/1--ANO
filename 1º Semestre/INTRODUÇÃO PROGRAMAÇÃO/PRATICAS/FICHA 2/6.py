#Elabore um programa que peça ao utilizador para introduzir sucessivas vezes um número inferior a 100 e que
#vá calculando o respectivo somatório, o qual vai ser escrito no ecrã, até que o valor desse somatório atinja ou
#ultrapasse o valor 500. Uma vez terminado esse ciclo deve ser escrito no ecrã a média dos valores válidos
#introduzidos.

somatorio= 0
controlo= 0

while somatorio <= 500:
    valor_introduzido= eval(input('Introduza um numero menor que 100:'))
    if valor_introduzido < 100:
        somatorio += valor_introduzido
        controlo += 1
        print('O somatorio é igual a', somatorio)
        print('O número de somas realizados é', controlo)
    else:
        print('Introduza un novo numero')    
        
print('A media dos somatorios é',somatorio/controlo)
        