def main():

    limiteinferior = int(input('Digite o limite inferior: '))
    limitesuperior = int(input('Digite o limite superior: '))

    for elemento in range(limiteinferior,limitesuperior+1):
        if elemento % 2 == 0:
            print(f'{elemento}')

main()   