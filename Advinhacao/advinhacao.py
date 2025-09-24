import random

def jogo_advinhacao():
    print(f'Bem vindo ao jogo de advinhação!')
    print(f'Tente advinhar o número de 1 a 10 que eu estou pensando...')

    numero_secreto = random.randint(1,10) # Gera um número aleatorio de 1 a 10

    while True:
        try:
            palpite = int(input(f'Digite um número: '))

            if palpite < 1 or palpite > 10:
                print(f'Digite um número entre 1 e 10.\n')
                continue
        
            if palpite == numero_secreto:
                print(f'Parabéns! Você acertou. O número era {numero_secreto}')
                break
            elif palpite < numero_secreto:
                print(f'Tente um número maior.\n')
            else: 
                print(f'Tente um número menor.\n')

        except ValueError:
            print('Entrada inválida! Digite apenas números inteiros.')

# Executar jogo
if __name__ =='__main__':
    jogo_advinhacao()


            