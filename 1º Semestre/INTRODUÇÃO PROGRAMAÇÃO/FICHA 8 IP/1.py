#Escreva uma função que pede ao utilizador para introduzir um valor entre um e vinte (1 e 20 inclusive) e se
#o número introduzido estiver fora desse intervalo, apresenta a mensagem “Número inválido”.

def retornar_numero_1_a_20 (numero):
    if numero >= 1 and numero <= 20:
        print('O número introduzido foi', numero)
    else:
        print('Número Invalido')
    return 

x= eval(input('Introduza um valor entre 1 e 20: '))

retornar_numero_1_a_20(x)