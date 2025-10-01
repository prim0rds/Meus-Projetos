# Sistema de Cálculo de Média de Notas

## Descrição
Este programa recebe 5 notas de um aluno, calcula a média e exibe:
- Maior nota
- Menor nota
- Situação do aluno

A situação do aluno é determinada de acordo com a média:
- Média >= 7 → Aprovado
- Média entre 5 e 6 → Recuperação
- Média < 5 → Reprovado

## Requisitos
- Python 3.8 ou superior

## Estrutura do Código
1. **Função calcular_media:**
   - Recebe uma lista de números.
   - Calcula a média usando `sum()` e `len()`.

2. **Entrada de notas:**
   - Solicita ao usuário 5 notas, uma por vez.
   - Valida se as notas estão entre 0 e 10.
   - Garante que somente números válidos sejam inseridos.

3. **Cálculo da média e situação:**
   - Calcula a média chamando a função `calcular_media`.
   - Verifica a situação do aluno usando `if/elif/else`.

4. **Exibição dos resultados:**
   - Mostra a média formatada com 1 casa decimal.
   - Exibe a maior e menor nota usando `max()` e `min()`.
   - Informa a situação do aluno.

## Exemplo de Uso
```
Digite a nota 1: 7
Digite a nota 2: 8
Digite a nota 3: 6
Digite a nota 4: 9
Digite a nota 5: 5

Sua média é: 7.0 → Você está aprovado.
Maior nota: 9
Menor nota: 5
```

## Observações
- O programa garante que o usuário digite apenas números válidos entre 0 e 10.
- O cálculo da média é automático e o programa se adapta a qualquer valor válido inserido.
- Pode ser facilmente adaptado para receber mais notas ou salvar resultados em arquivo.

## Próximos Passos (opcional)
- Tornar o número de notas variável, perguntando ao usuário quantas notas deseja informar.
- Salvar histórico de notas em arquivo externo.
- Adicionar interface gráfica para facilitar a interação.

