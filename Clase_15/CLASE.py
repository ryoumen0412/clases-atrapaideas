def duplicarNumeros(num):
    '''
    FUNCION PARA DUPLICAR NUMEROS...
    '''
    numDuplicado = num*2
    return numDuplicado

print(duplicarNumeros.__doc__)
num = float(input('aaa... '))
numDup = duplicarNumeros(num)
print(numDup)

def empanadas(palabra):
    otra_palabra = palabra*2 + ' de pino'
    return otra_palabra

print(empanadas('masa'))

def mult(num1, num2, num3):
    output = num1*num2*num3
    return output

aeiou=mult(123, 65, 456)
print(aeiou)

def func(inputt):
    longitud = len(inputt)
    contador = inputt.lower().count('a')
    return longitud, contador

print(func('Alabama'))

oeo = 'Atalaya'

eo, oe = func(oeo)

print(f'La palabra {oeo} tiene {eo} letras y {oe} ases')