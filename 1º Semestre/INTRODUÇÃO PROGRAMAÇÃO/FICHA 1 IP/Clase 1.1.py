#1

x= eval(input('escreva o valor minimo:'))
y= eval(input('escreva o valor maximo'))

#2
def convert_F_C(F):

while x <= y:
    print(x,'F', convert_F_C(x),'C')
    x = x + 1
    
def convert_F_C(F):
    Celsius = 5 * (F-32)/9
    return Celsius
