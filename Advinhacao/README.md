# Projeto: Jogo de Adivinhação em Python

## Descrição
Este programa é um jogo de adivinhação em que o usuário tenta descobrir o número que o computador escolheu aleatoriamente entre 1 e 10.  
O programa dá dicas se o palpite é maior ou menor que o número secreto e valida a entrada para aceitar apenas números inteiros.

## Funcionalidades
- Gera um número aleatório entre 1 e 10.
- Permite que o usuário tente adivinhar até acertar.
- Dá dicas se o palpite é maior ou menor.
- Trata entradas inválidas (letras ou caracteres especiais).
- Estruturado em função para melhor organização.

## Tecnologias utilizadas
- Python 3

## Como executar
1. Clone este repositório ou baixe o arquivo `adivinhacao.py`.
2. Abra o terminal (ou prompt de comando).
3. Execute o programa com:
   ```bash
   python adivinhacao.py
   ```
4. Digite seu palpite quando solicitado.

## Estrutura do projeto
```
Adivinhacao/
│
├── adivinhacao.py   # Código principal
└── README.md        # Documentação
```

## Exemplo de uso
```
Bem-vindo ao Jogo de Adivinhação!
Tente adivinhar o número que estou pensando entre 1 e 10.

Digite seu palpite: 5
Tente um número maior.

Digite seu palpite: 8
Parabéns! Você acertou! O número era 8.
```

## Aprendizados
- Uso de loops (`while`) para repetição até acertar.
- Estruturação de código em funções.
- Geração de números aleatórios com `random`.
- Validação de entrada e tratamento de erros.
