# Objetivo: Criar um programa que receba 5 notas e calcule a média, mostrando a maior e a menor nota
# Notas de 0 a 10. >=7 aprovado, 5-6 recuperação, <5 reprovado

# Criação da função média:
def calcular_media(numeros):
    if len(numeros) == 0: # Evita divisão por zero
        return 0
    return sum(numeros) / len(numeros)


# Inserção de notas com validação
notas = []
while len(notas) < 5:
    try:
        nota = float(input(f'Digite a nota {len(notas)+1}: '))
        if 0 <= nota <= 10:
            notas.append(nota)
        else:
            print("Digite uma nota entre 0 e 10.")
    except ValueError:
        print("Digite somente números válidos.")

media = calcular_media(notas)


# Situação do aluno
if media >= 7:
    situacao = "aprovado"
elif 5 <= media < 7:
    situacao = "de recuperação"
else:
    situacao = "reprovado"

print(f"\nSua média é: {media:.1f} → Você está {situacao}.")
print(f"Maior nota: {max(notas)}")
print(f"Menor nota: {min(notas)}")







