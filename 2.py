#função
def divisão(dividido,divisor):
    if divisor==0:
        print('não é possível utilizar 0 para dividir nenhum número')
        resposta=False
    elif dividido%divisor==0:
        resposta=True
    else:
        resposta=False
    return resposta

#main

dividido=int(input('digite um número inteiro que deseja dividir: '))
divisor=int(input('digite um número inteiro para ser o divisor: '))
resposta=divisão(dividido,divisor)
print(resposta)