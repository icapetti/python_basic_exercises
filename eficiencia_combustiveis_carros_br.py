# O programa recebe o valor de km/litro e converte em litros/100 km
# Exibe o resultado formatado em duas casas decimais

km_l = float(input())

if(km_l != 0):
    l_100km = 100/km_l
else:
    print("O valor de Km/L deve ser maior que 0")

print("{:.2f}".format(l_100km))