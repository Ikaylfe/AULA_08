def dobro(a):
    r= a*2
    return r


def quadrado(a):
    q= a*a
    # q= a**2 ( tbm uma forma de usar a raiz de um número - o asterístico significa expoente)
    return q



n1= int(input('Número 1: '))

resposta=dobro(n1)
print(f'O dobro de {n1} é:\n{resposta}')

resposta=quadrado(n1)
print(f'O quadrado de {n1} é: \n{resposta}')

# -------------------------------------------
