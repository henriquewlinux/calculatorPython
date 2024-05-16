def somar(x, y):
    return x + y

def subtrair(x, y):
    return x - y

def multiplicar(x, y):
    return x * y

def dividir(x, y):
    if y != 0:
        return x / y
    else:
        return "Erro: Divisao por zero"

def main():
    while True:
        print("Opcoes:")
        print("Digite '1' para somar dois numeros")
        print("Digite '2' para subtrair dois numeros")
        print("Digite '3' para multiplicar dois numeros")
        print("Digite '4' para dividir dois numeros")
        print("Digite 'sair' para sair do programa")
        
        opcao = input("Digite a operacao que deseja realizar: ")

        if opcao == "sair":
            print("Saindo do programa...")
            break
        elif opcao in ('1', '2', '3', '4'):
            num1 = int(input("Digite o primeiro numero: "))
            num2 = int(input("Digite o segundo numero: "))
            print(' ')

            if opcao == '1':
                print("Resultado: {}".format(somar(num1, num2)))
            elif opcao == '2':
                print("Resultado: {}".format(subtrair(num1, num2)))
            elif opcao == '3':
                print("Resultado: {}".format(multiplicar(num1, num2)))
            elif opcao == '4':
                resultado = dividir(num1, num2)
                print("Resultado: {}".format(resultado))
            print(' ')
            print(' ')
        else:
            print(' ')
            print("Opcao invalida! Tente novamente.")
            print(' ')

if __name__ == "__main__":
    main()