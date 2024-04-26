def main():

    numero = int(input('Digite um numero: '))

    soma = 0

    for elemento in range(1,numero+1):
        soma += elemento

    print(f'A soma dos elementos é {soma}')

main()