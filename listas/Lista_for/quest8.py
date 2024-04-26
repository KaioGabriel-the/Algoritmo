def main():

    numero = int(input('Digite um numero: '))
    limiteinferior = int(input('Digite o limite inferior: '))
    limitesuperior = int(input('Digite o limite superior: '))

    for elemento in range(limiteinferior,limitesuperior+1):
        if elemento % numero  == 0:
            print(f'{elemento}')

main()