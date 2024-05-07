def main():

    frase = str(input('Digite sua frase: '))

    frase_nova = ''
    for i in range(0,len(frase)):

        if frase[i] == '1':
            frase_nova += 'um'
        elif frase[i] == '2':
            frase += 'dois'
        elif frase[i] == '3':
            frase += 'três'
        elif frase[i] == '4':
            frase += 'quatro'
        elif frase[i] == '5':
            frase += 'cinco'
        elif frase[i] == '6':
            frase += 'seis'
        elif frase[i] == '7':
            frase += 'sete'
        elif frase[i] == '8':
            frase += 'oito'
        elif frase[i] == '9':
            frase += 'nove'
        else:
            frase += str(frase[i])
    
    print(f'{frase_nova}')

main()