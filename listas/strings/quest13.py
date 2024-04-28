def main():

    nome = str(input('Digite o nome: ')).upper()
    incio = nome.split(' ')

    inicias = ''
    for i in range(0,len(nome)):
        if nome[i] == ' ':
            inicias += str(nome[i+1])+(".")

    print(f'{incio[(len(incio)-1)]},{nome[0]}.{inicias}')

main()