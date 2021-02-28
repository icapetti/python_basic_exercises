# Le um numero inteiro e exibe a soma dos digitos desse numero

num = input()
result = 0
for i in range(len(num)):
    result = result + int(num[i])

print(result)