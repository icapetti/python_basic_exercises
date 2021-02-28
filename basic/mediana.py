# Calcula e retorna a mediana de três valores passados por argumento.

def mediana(a, b, c):
    valores = [a, b, c]
    valores.sort()
    return valores[1]

print(mediana(5, 2, 6))