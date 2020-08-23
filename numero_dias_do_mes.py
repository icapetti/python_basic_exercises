# O programa define uma funcao que retorna o número de dias de um dado mês.
# O mês é indicado por um número entre 1 e 12, sendo 1 o mês de janeiro. 
# A sua função deve também receber um argumento opcional chamado bissexto de valor padrão False. 
# Quando o valor do argumento bissexto é True considere fevereiro com 29 dias, senão 28.

months = {
    '1': 31,
    '2': 28,
    '3': 31,
    '4': 30,
    '5': 31,
    '6': 30,
    '7': 31,
    '8': 31,
    '9': 30,
    '10': 31,
    '11': 30,
    '12': 31,
}

def dias(mes, bissexto = False):
    mes = str(mes)
    if(mes == "2" and bissexto == True):
        return months[mes] +1
    else:
        return months[mes]

print(dias(10))