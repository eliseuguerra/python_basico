"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
while True:
    try:
        valor = int(input('Informe um numero: '))
        break

    except: 
        print('Entrada Invalida! Digite novamente:')

if valor % 2 == 0:
    print('Numero par')
else:
    print('Numero impar')    
