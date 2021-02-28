# O programa define uma funcao que recebe dois valores e retorna o maior deles.

def maior(a,b):
    if(a > b):
        return a
    else:
        return b

a, b = map(int, input().split())

print(maior(a,b))