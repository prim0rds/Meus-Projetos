# Sistema de Login Simples em Python

## Descrição
Este é um **sistema de login simples em Python** que utiliza um **arquivo externo (`usuarios.txt`)** para armazenar usuários e senhas.
O sistema permite:
- Login com senha escondida (`*`) usando a biblioteca `pwinput`.
- Limite de tentativas (padrão: 3).
- Tratamento de erros com `try/except`.

## Requisitos
- Python 3.8 ou superior
- Biblioteca `pwinput`

Instalação da biblioteca:
```
pip install pwinput
```

## Estrutura de Arquivos
```
sistema_login/
│
├─ sistema_login.py        # Script principal do sistema de login
├─ usuarios.txt            # Arquivo externo com usuários e senhas
└─ README.pdf              # Este README em PDF
```

## Formato do arquivo `usuarios.txt`
Cada linha deve conter um usuário e senha separados por vírgula:
```
admin,12345
felipe,python123
maria,senha123
```
- Sem espaços antes ou depois da vírgula.
- Pode ter várias linhas para múltiplos usuários.

## Como usar
1. Certifique-se de ter Python 3 instalado.
2. Instale a biblioteca `pwinput`:
```
pip install pwinput
```
3. Abra o terminal na pasta do projeto.
4. Execute o script:
```
python sistema_login.py
```
5. Digite o login e a senha quando solicitado.
6. O sistema permite até 3 tentativas antes de bloquear o login.

## Observações
- Este sistema **não criptografa senhas**. Para produção, é recomendado usar **hashing** (ex.: `bcrypt`).
- Se o arquivo `usuarios.txt` não existir, o sistema exibirá um aviso e encerrará.
- Pressionar `Ctrl+C` interrompe o programa de forma segura.

## Próximos Passos (opcionais)
- Implementar cadastro de novos usuários diretamente no arquivo TXT.
- Salvar senhas criptografadas usando `bcrypt`.
- Migrar para JSON ou banco de dados para maior escalabilidade.

