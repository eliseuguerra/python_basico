"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

while True:
    try:
        hora_str = input('Digite a hora: ')
        hora = int(hora_str)
        if 0 <= hora <= 23:
            break
        else:
            print('Entrada invalida! Digite somente numeros inteiros.')
    except:
        print('Digite a hora (apenas numero 0 - 23):')
if 6 <= hora < 12:
    print('Bom dia') 
elif 12 <= hora < 18:
    print('Boa tarde') 
elif 18 <= hora < 23:
    print('Boa noite')                  
    