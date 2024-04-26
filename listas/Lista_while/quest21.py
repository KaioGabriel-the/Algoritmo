def main():
    numero = int(input('DIGITE UM NUMERO: '))
    numero2 = int(input('DIGITE OUTRO NUMERO: '))

    soma = 0
    qtd_soma = 0

    while qtd_soma != numero2 :
        soma += numero
        qtd_soma += 1

    print(f'{soma}')

main()
