# O programa le um numero inteiro n e exibe a soma dos n primeiros inteiros positivos

n = int(input())
resultado = 0
for i in range(1, n+1):
    resultado = resultado + i

print(resultado)