#indicativa se o aluno foi aprovado ou não, juntamente com a média obtida. O aluno fica aprovado se a média
#for superior ou igual a 9.5. O seu programa deverá gerar uma interação como a seguinte (exemplo):
#Escreva a primeira nota: 15
#Escreva a segunda nota: 10
#Aprovado. Com média de: 12.5

#1 

def verificar_aprovação(nota1, nota2):
    media= (nota1 + nota2) / 2
    if media >= 9.5:
        print('Aprovado. Com média de:',media)
        
    else:
        print('Reprovado. Com media de:',media)
        
    return

nota1= eval(input('Escreva a primeira nota: '))
nota2= eval(input('Escreva a segunda nota: '))
print(verificar_aprovação(nota1, nota2))
        
