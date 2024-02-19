#Elabore um programa que peça ao utilizador para introduzir sucessivas vezes um número inferior a 100 e que
#vá calculando o respectivo somatório, o qual vai ser escrito no ecrã, até que o valor desse somatório atinja ou
#ultrapasse o valor 500. Uma vez terminado esse ciclo deve ser escrito no ecrã a média dos valores válidos
#introduzidos.


soma= 0
controlador= 0

while soma <= 500:
    
    inferior= eval(input('Escreva um número inferior a 100:'))
    
    if inferior > 0 and inferior <= 100:
        soma+= inferior
        print('somatorio:', soma) 
        controlador+= 1
    else: 
        print('valor não aceite')
        
print('A media é: ', soma/controlador)    
        