def empanada(numero):
    '''
    Revisa si el numero ingresado es 5
    '''
    if numero==5:
        return True
    else:
        return False
    
resultado = empanada(5)
print(resultado)

def anticucho(palabrota):
    '''
    concatenar la palabrota en minusculas 5 veces
    '''
    resultado = palabrota.lower()*5
    
    return resultado

print('+'*90)

palabritas = anticucho('Alejandro')

print(palabritas)

