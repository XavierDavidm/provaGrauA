#função
def divisivel(n):
    n=int(input('digite um número inteiro para saber se ele é divisível por 2: '))
    if n%2 ==0:
        resposta=True
    else:
        resposta=False
    return resposta

#main
n=0
resposta=0
resposta=divisivel(n)
print(resposta)