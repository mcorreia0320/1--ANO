#1

segundos = eval(input('Escreva uma quantidade de segundos'))

#2 

dias = (segundos//86400)
sobrante1= (segundos % 86400)

horas= (sobrante1 // 3600)
sobrante2= (sobrante1 % 3600)

minutos= (sobrante2 // 60)
sobrantes3= (sobrante2 % 60) #segundos

#3

print('dias:',dias, 'horas:', horas, 'minutos:', minutos, 'segundos:', sobrantes3)





