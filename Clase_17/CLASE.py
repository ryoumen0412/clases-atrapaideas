# numero1 = int(input('Ingrese el primer numero... '))

# numero2 = int(input('Ingrese el segundo numero... '))

# division = numero1/numero2

# print(f'La division entre {numero1} y {numero2} es {division:.2f}...')

# numero1 = float(input('Ingrese el primer numero... '))

# numero2 = float(input('Ingrese el segundo numero... '))

# if numero2 == 0:
#     print('NO SE PUEDE DIVIDIR POR CERO!!')
# else:
#     division = numero1/numero2
#     print(f'La division entre {numero1} y {numero2} es {division:.2f}...')
    

try:
    numero1 = int(input('Ingrese el primer numero... '))
    numero2 = int(input('Ingrese el segundo numero... '))
    division = numero1/numero2
    print(f'La division entre {numero1} y {numero2} es {division:.2f}...')
# except Exception as e:
#     print(f'{e}')
except ZeroDivisionError as z:
    print(f'No se puede dividir por cero: {z}')
except ValueError as v:
    print(f'Valor invalido: {v}')
    


