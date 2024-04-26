import random

def main():

    numero = random.randint(0, 100)
    numero_02 = ''

    while numero != numero_02:
        numero_02 = int(input('Digite numero: '))
        if numero_02 > numero:
            print(f'Numero menor')
        elif numero_02 < numero :
            print('Numero maior')
    print('Parabens!!!')


main()
