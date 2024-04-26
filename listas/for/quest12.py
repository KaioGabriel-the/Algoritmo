def main():

    numero = int(input('Digite um numero: '))

    for elemento in range (1,2):

        print('''DIGITE SUA LISTA''')

        lista = int(input('Primeiro elemento da sua lista: '))
        soma = lista
        giros = 1

        while lista != 0:


            lista =int(input('Primeiro elemento da sua lista: '))
            giros += 1
            soma += lista

    
    print(f'''Soma:{soma}
              Media:{soma/giros}''')

main()
