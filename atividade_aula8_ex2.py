def multa(a):
    m = (a-100)*4
    return m

total= float(input('Informe peso da pesca:'))


if total >= 100:    
        print(f'Total excede limite de peso, valor a pagar = {multa(total)}.')
else:
        print(f'O total pescado {total} dentro do limite permitido')






     
    




