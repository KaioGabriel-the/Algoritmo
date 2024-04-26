def main():
    numero = int(input('DIGITE UM NUMERO: '))
    numero2 = int(input('DIGITE OUTRO NUMERO: '))

    soma = 0
    contador = 0
    while soma <= numero:
        soma += numero2
        contador += 1

    new_contador = contador -1
    resto = numero - new_contador*numero2
    print(f'resultado:{new_contador} resto:{resto} ')

main()