# Sistema de login simples #

# Utilizando pwinput para esconder a senha
import pwinput as pw

# Função para carregar usuários de arquivo TXT
def carregar_usuarios(arquivo):
    usuarios = {}
    try:
        with open(arquivo, 'r', encoding='utf-8') as f:
            for linha in f:
                usuario, senha = linha.strip().split(',')
                usuarios[usuario] = senha
    except FileExistsError:
        print(f'Arquivo {arquivo} não encontrado!')
    except Exception as e:
        print(f'Erro ao ler o arquivo: {e}')
    return usuarios
    
# Carregar usuários do arquivo
usuarios = carregar_usuarios('usuarios.txt')
if not usuarios:
    print(f'Nenhum usuário carregado. Encerrando o programa.')
    exit()

# Definindo limite de tentativa de login
tentativa_login = 0
limite_tentativas = 3

# Loop de login
while tentativa_login < limite_tentativas:
    # Entrada do usuário
    usuario = input('Digite seu login: ')
    senha = pw.pwinput('Digite sua senha: ')

    if usuario in usuarios and senha == usuarios[usuario]:
        print(f'Olá.\nBem vindo!')
        break
    else:
        tentativa_login += 1 
        restantes = limite_tentativas - tentativa_login
        print(f'Login ou senha incorretos.\nTentativas restantes: {restantes}.')

if tentativa_login == limite_tentativas:
    print('Número máximo de tentativas atingido.\nLogin bloqueado.')


