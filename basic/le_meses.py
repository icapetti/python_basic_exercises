# O programa recebe uma lista de nome de meses e retorna o numero correspondente a cada mes.
# Para sinalizar o fim da lista deve-se digitar fim

# Define o dicionario dos meses
months = {
    'janeiro': 1,
    'fevereiro': 2,
    'março': 3,
    'abril': 4,
    'maio': 5,
    'junho': 6,
    'julho': 7,
    'agosto': 8,
    'setembro': 9,
    'outubro': 10,
    'novembro': 11,
    'dezembro': 12,
}

# Define uma lista para aguardar os meses digitados e uma variavel de controle do fluxo
list_month = []
month = ""

# Enquanto o mes digitado for diferente de fim o programa solicitara um input
while (month != "fim"):
    month = input().lower() # Armazena o input na variavel tratando a string como minuscula
    list_month.append(month) # Adiciona o mes informado na lista de meses

# Laco percorre toda a lista de meses informados e verifica se o mes informado esta contido no dicionario.
# Se estiver eh mostrado o numero do respectivo mes.
for i in range(len(list_month)-1):
    if(list_month[i] in months):
        print(months[list_month[i]])