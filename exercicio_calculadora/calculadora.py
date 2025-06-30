print("Bem-vindo à calculadora em Python!")
print("Escolha a operação:")
print("1. Soma (+)")
print("2. Subtração (-)")
print("3. Multiplicação (*)")
print("4. Divisão (/)")
print("5. Sair")

while True:
    escolha = input("Digite sua escolha (1/2/3/4/5): ")

    if escolha in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
        except ValueError:
            print("Entrada inválida. Por favor, digite apenas números.")
            continue

        if escolha == '1':
            resultado = num1 + num2
            print(f"{num1} + {num2} = {resultado}")
        elif escolha == '2':
            resultado = num1 - num2
            print(f"{num1} - {num2} = {resultado}")
        elif escolha == '3':
            resultado = num1 * num2
            print(f"{num1} * {num2} = {resultado}")
        elif escolha == '4':
            if num2 == 0:
                print("Erro! Divisão por zero.")
            else:
                resultado = num1 / num2
                print(f"{num1} / {num2} = {resultado}")
    elif escolha == '5':
        print("Saindo da calculadora. Até mais!")
        break
    else:
        print("Opção inválida. Por favor, digite uma escolha válida (1/2/3/4/5).")