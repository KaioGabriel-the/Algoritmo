def main():

    palavra = str(input('Digite a palavra: '))
    palavra_invertida = palavra[: :-1]

    if palavra == palavra_invertida:
        print(f'A palavra é um palíndroma')
    else:
        print(f'A palavra não é um palíndroma')

main()
