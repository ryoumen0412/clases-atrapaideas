import math
import numpy as np


# PARTE 1
# 1.

def x1(x):
    # a
    y = x*2
    return y

print(x1(2))

def x2(x):
    # b
    y = 3*x+2
    return y

print(x2(2))

def x3(x):
    # c
    y = x^3
    return y

print(x3(2))

def x4(x):
    # d
    y = x*x-100
    return y

print(x4(2))

def x5(x):
    # e
    y = math.sqrt(x)
    return y

print(x5(9))

# 2.
print('+'*90)

def xa(x, y):
    # a
    z = x+y
    return z

print(xa(4,5))

def xb(x, y):
    # b
    z = x-y
    return z

print(xb(5,4))

def xc(x, y):
    z = x*y
    return z

print(xc(5,4))

def xd(x, y):
    z = y*y-x
    return z

print(xd(5,4))

def xe(x, y):
    z = math.sqrt((x*x)+(y*y))
    return z

print(xe(5,4))

def xf(x, y):
    z = ((x**3)+2*x*y+(y**3))**(1/3)
    return z

print(xf(5,4))

def xg(x, y):
    z = x % y
    return z

print(xg(5,4))

def xh(x, y):
    z = x**y
    return z

print(xh(5,4))

# 3.

arreglo = np.array([1,2,3,4,5])
arreglo2 = np.array([2,3,4,5,6])

tres = xg(arreglo,arreglo2)

print(tres)

print('''
    SI FUNCIONAN :D
''')

print('+'*90)

# PARTE 2

# 1.

def stringPorDos(string):
    stringXDos = string*2
    return stringXDos

print(stringPorDos('Eo'))

# 2.

def stringLower(string):
    string_lower = string.lower()
    return string_lower

print(stringLower('AAAAAAAAA'))

# 3.

def stringMulti(string, integer):
    multi = string*integer
    return multi

print(stringMulti('aE', 4))

# 4.

def verifCorreo(correo):
    
    if '@' in correo and '.com' in correo:
        valido = True
    else:
        valido = False
    
    return valido

print(verifCorreo('alejandro@gmail.com'))
print(verifCorreo('aaaaaaaaa'))

# 5.

