# Criar um algoritmo onde o usuário fornece um número e o algoritmo entrega a tabuada de 1 a 10 do mesmo.

# Definindo a função tabuada
def tabuada(num):
    print(f'\nA tabuada do {num} até 10: ')
    for n in range(1,11):
        resultado = num * n
        print(f'{num} x {n} = {resultado}')

# Loop para garantir que o usúario digite apenas números inteiros
while True:
    try:
        num = int(input('Digite um número inteiro: '))
        break # Sai do loop se a entrada for válida
    except ValueError:
        print(f'Entrada inválida! Digite apenas números inteiros.\n')


# Invocando a função
tabuada(num)





