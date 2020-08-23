# O programa realiza as operacoes aritmeticas basicas: soma, subtracao, divisao e multiplicacao

op, a, b = input().split()
a = int(a)
b = int(b)

if(op == "+"):
    resultado = a + b
elif(op == "-"):
    resultado = a - b
elif(op == "*"):
    resultado = a * b
elif(op == "/"):
    if(b != 0):
        resultado = a/b
    else:
        resultado = "impossivel divisao por zero"
else:
    resultado = "informe uma operacao valida: + - * /"

print(resultado)
