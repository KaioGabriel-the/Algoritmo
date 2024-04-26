def main():

    numero = int(input('Digite o limite: '))

    soma = 1
    for elemento in range (numero+1):
        soma+= elemento
        print(f'''{elemento + soma} ''')

main()