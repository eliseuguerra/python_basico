name = input("Digite seu nome: ")
age = input("Digite sua idade: ")

if name and age:
    print(f'Seu nome é {name}')
    print(f'Seu nome invertido é {name[::-1]}')
    print(f'Sua idade é {age}')

    if ' ' in name:
        print('Seu nome contém espaço')
    else:
        print('Não contém espaços')  
    print(f'Seu nome tem {len(name)} letras')  
    print(f'A primeira letra é {name[0]}')   
    print(f'A ultima letra é {name[-1]}')   
else:
    print('voce deixou o campo')    

 
