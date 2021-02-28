# O programa realiza a soma de dois numeros reais e exibe o resultado formatado com duas casas decimais

a, b = map(float, input().split())
resultado = a + b
print("{:.2f}".format(resultado))