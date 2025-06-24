"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva Add commentMore actions
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
while True:
    nome = input("Por favor, digite seu primeiro nome: ")

    if nome.strip():
        break 
    else:
        print("Nome inválido! Por favor, digite seu nome (não pode ser vazio).")

numero_letras = len(nome.strip())


if numero_letras <= 4:
    print("Seu nome é curto.")
elif 5 <= numero_letras <= 6:
    print("Seu nome é normal.")
else: # Se não for <= 4 e nem entre 5 e 6, só pode ser > 6
    print("Seu nome é muito grande.")