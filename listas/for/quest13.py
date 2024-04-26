def main():

    numero = int(input('Digite um numero: '))

    for elemento in range(0,1):

        elemento += elemento
        
        maior = 0
        lista = 1
        while lista != 0:

            lista = int(input('Digite um item da sua lista: '))
        
            if lista > maior:
                maior = lista

        print(f'Maior:{maior}')

main()
