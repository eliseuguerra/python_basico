# Operadores logicos 'and' / 'or'
#if 1 and 1:
#    print(True and 1 and False)

entrada = input("[E]ntrar ou [S]air: ") 
senha = input('Digite senha: ')   
senha_permitida = '12345'

if (entrada == 'E' or entrada == 'e') and senha == senha_permitida:
    print('entrada permitida')
else:
    print('Senha errada!')    
