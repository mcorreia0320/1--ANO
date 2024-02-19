#Escreva um programa em Python que lê o número de horas, que um empregado trabalhou numa dada semana e o seu salário/hora e calcula 
#o ordenado semanal tendo em conta as horas extraordinárias. 
#O salário é calculado do seguinte modo: se o número de horas for menor que 40, então o salário é dado pelo produto do número de horas pelo 
# salário hora, em caso contrário recebe horas extraordinárias as quais são pagas a dobrar. 

#1 

horas_por_semana= eval(input('Escreva o numero de horas trabalhadas numa semana:'))
salario_por_hora= eval(input('Escreva o salario por hora:'))

#2 

if horas_por_semana < 40:
    print('salario:', horas_por_semana * salario_por_hora ,'€ semanal')
    
else:
    horas_extras= eval(input('Escreva horas extraordinárias trabalhadas:'))
    horas_extras= horas_extras * 2
    print('salario:',( (horas_por_semana + horas_extras) * salario_por_hora),'€ semanal')

