# O programa refine uma funcao que recebe os parametros de uma corrida de taxi e retorna o custo dela.
# Parametros: km, valor por 200 metros rodados (padrao eh 0.50) e largada (padrao eh 4.00)
# O calculo do custo eh largada + valor (a cada 200 metros)

def tarifa(km, largada=4, valor=0.50):
    return largada + ((km*1000)/200)*valor 

print(tarifa(1))