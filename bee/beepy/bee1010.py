def main():

    lista = []
    lista2 = []

    lista = input('').split(' ')
    lista2 = input('').split(' ')

    peca1 = int(lista[1])*float(lista[2])
    peca2 = int(lista2[1])*float(lista2[2])
    soma = peca1 + peca2

    print(f'VALOR A PAGAR: R$ {soma:.2f}')

main()