'''
PARTE 1
------------------
1.
'''


try:
    edad = int(input('Ingrese su edad... '))

    if edad<18:
        print('Menor de edad...')
    else:
        print('Mayor de edad!!!')
except Exception as e:
    print(e)
    
'''
2.
'''

try:
    num1 = float(input('Waiting for number... '))
except Exception as e:
    print(e)
    

try:
    num2 = float(input('Waiting for number... '))
except Exception as e:
    print(e)

try:
    op = str(input('Waiting for operation: + - / *... '))
except Exception as e:
    print(e)
    
try:
    match op:
        case '+':
            result = num1 + num2
            print(result)
        case '-':
            result = num1 - num2
            print(result)
        case '/':
            result = num1 / num2
            print(result)
        case '*':
            result = num1 * num2
            print(result)
        case _:
            print('Invalid operator...')
except Exception as e:
    print(e)

'''
3.
'''

def strToFloat(string):
    
    try:
        float_ = float(string)
        return float_
    except Exception as e:
        
        Error = f'None. \n\n{e}'
        return Error

string1 = input('Ingrese un numero... ')

float1 = strToFloat(string1)

print(float1)

if type(float1) == float:
    print(type(float1))
else: 
    print('Exception...')

'''
4.
'''

lista = [1,'2',3,4,'5',6,'hola']

def mutateToFloat(array):
    
    length = len(array)
    lista = []
    
    for i in range(length):
        try:
            convValue = float(array[i])
        except:
            convValue = None
        lista.append(convValue)
    
    return lista

listaFloat = mutateToFloat(lista)
print(listaFloat)

