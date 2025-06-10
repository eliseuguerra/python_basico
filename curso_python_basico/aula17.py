#Operadores relacionais

vl_1 = int(input('Digite um valor: '))
vl_2 = int(input('Digite um segundo valor: '))
soma = vl_1 + vl_2

if soma <= 18:
    print('menor')
elif 18 < soma <= 50:
    print('maior')  
else:
    print('idoso')      
