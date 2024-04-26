def calcular_binario(numero):

    if numero == 0:
        return '0'
    
    binario = ''
    numero = numero
    while numero > 0:
        resto = numero % 2
        binario = str(resto) + binario
        numero = numero // 2

    return binario

def  identificador_hexadecimal(resto):
    
    if resto == 0:
        return 0
    elif resto == 1:
        return 1
    elif resto == 2:
        return 2
    elif resto == 3:
        return 3
    elif resto == 4:
        return 4
    elif resto == 5:
        return 5
    elif resto == 6:
        return 6
    elif resto == 7:
        return 7
    elif resto == 8:
        return 8
    elif resto == 9:
        return 9
    elif resto == 10:
        return 'A'
    elif resto == 11:
        return 'B'
    elif resto == 12:
        return 'C'
    elif resto == 13:
        return 'D'
    elif resto == 14:
        return 'E'
    else:
        return 'F'


def calcular_hexadecimal(numero):

    if numero == 0 :
        return '0'
    hexadecimal =''
    numero = numero
    while numero > 0:
        resto = numero % 16
        hexadecimal = str(identificador_hexadecimal(resto)) + hexadecimal
        numero = numero // 16
        
    
    return hexadecimal
    
def main():

    numero = int(input('DIGITE UM NUMERO (ENTRE 0 255):'))

    binario = calcular_binario(numero)
    hexadecimal = calcular_hexadecimal(numero)
    
    print(f'{numero} em binario:{binario}... {numero} em hexadecimal:{hexadecimal}')
    
main()