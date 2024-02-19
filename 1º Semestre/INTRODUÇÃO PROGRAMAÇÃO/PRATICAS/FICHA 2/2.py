#Implemente um programa em Python que lê duas notas introduzidas pelo utilizador e imprime uma mensagem
#indicativa se o aluno foi aprovado ou não, juntamente com a média obtida. O aluno fica aprovado se a média
#for superior ou igual a 9.5. O seu programa deverá gerar uma interação como a seguinte (exemplo):

#Escreva a primeira nota: 15
#Escreva a segunda nota: 10
#Aprovado. Com média de: 12.5

#1

def calcular_media(nota_1,nota_2):
    media = (nota_1 + nota_2) / 2
    return media

while True:
    nota1 = eval(input('Escreva a primeira nota: '))
    nota2 = eval(input('Escreva a segunda nota: '))
    
    if nota1 > 0 and nota1 <=20 and nota2 >0 and nota2 <=20:
        media= calcular_media(nota1, nota2)
        if media >= 9.5:
            print('Aprovado. Com média de:', media)
            break
            
        else:
            print('Reprovado. Com média de:', media)
            break
            
    else: 
        print('Valores incorrectos, tente de novo')
    