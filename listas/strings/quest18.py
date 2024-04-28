def main():

    frase = (str(input('Digite --> '))).split(' ')

    print(f'O que deseja subistituir???')

    for i in range(0,len(frase)):
        print(f'{i} --> {frase[i]}')

    substituir = int(input('Digite o numero do que você deseja substituir: '))
    frase[substituir] = str(input('Digite a nova palavra no lugar:'))

    nova = ''

    for i in range (0,len(frase)):
        nova += str(frase[i] + ' ')

    print(f'{nova}')

main()