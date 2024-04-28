def main():

    frase = str(input('Digite --> '))
    
    print(f'{frase}')

    inicio = int(input('Posição inicial: '))
    final = int(input('Posição final: '))

    new = ''
    for inicio in range(inicio,final+1):
        new+= str(frase[inicio])
        inicio += 1
    print(f'{new}')

main()