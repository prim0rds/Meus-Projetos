# Inputs do usuário
num1 = int(input('Bem vindo a calculadora, para começarmos digite o primeiro número: '))
operacao = input('Digite a operação desejada: ')
num2 = int(input(f'Digite o segundo número: '))

# Criação das operações
match operacao:
    case "+":
        res = num1 + num2
    case "-":
        res = num1 - num2
    case "/":
        res = num1 / num2
    case "*":
        res = num1 * num2

# Imprimindo resultado
print(f'O resultado de {num1}{operacao}{num2} é {res}')