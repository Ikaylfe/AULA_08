def calcula_imc(p,a):
    i=p/(a**2)
    return i



qtd= int(input('Informe a qtde de pessoas:'))
for i in range(qtd):
    print(f'\nPessoa{i+1}')
    peso=float(input('Informe o peso:'))
    altura=float(input('Informe a altura:'))

    imc=calcula_imc(peso,altura)


    match imc:
        case imc if imc < 17:
            classificacao = 'Muito Abaixo'
        case imc if imc < 18.5:
            classificacao = 'Abaixo Abaixo'
        case imc if imc < 25:
            classificacao = 'Peso Normal'
        case imc if imc < 30:
            classificacao = 'Acima do peso'
        case imc if imc < 35:
            classificacao = 'Obesidade grau I'
        case imc if imc < 40:
            classificacao = 'Obesidade grau II'
        case _:
            classificacao = 'Obesidade grau III'


# Saída
print(30* "=")
print('Resultado')
print(f'IMC= {imc: .2f}')
print(f'Classificação : {classificacao}')