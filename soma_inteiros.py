# O programa realiza a soma de dois numeros inteiros
# Recebe os dois numeros inteiros em uma unica linha separados por 1 espaco
# Utiliza o split() para dividir essas valores e atribuir as variaveis de cada um.
# Utiliza em conjunto ao split() o map() e int para converter o valor de input().

a, b = map(int, input().split())
print(a+b)