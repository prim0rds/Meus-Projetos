# Definindo o contador de vogais
def contar_vogais(texto):
    vogais = 'aeiou'
    contador = 0
    for letra in texto.lower():
        if letra in vogais:
            contador +=1
    return contador

# Input do usuário
texto = str(input('Digite uma palavra: '))
       
# Resultado do algoritmo
resultado = contar_vogais(texto)
print(f'O {texto} possui {resultado} vogais.')


    