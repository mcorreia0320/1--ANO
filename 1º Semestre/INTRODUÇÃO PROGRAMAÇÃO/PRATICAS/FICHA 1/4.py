#1 

distancia= eval(input('Escreva uma distancia:'))
tempo= eval(input('Escreva o tempo para recorrela:'))

#2

horas= (tempo//60)
metros=(distancia*1000)
segundos=(tempo*60)

#3 calcular media

a= distancia//horas
b= metros/segundos

#4

print('a.', a,'km/h', '\nb.', b, 'm/s')