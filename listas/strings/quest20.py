def main():

    frase = (str(input('Digite uma frase: '))).lower()

    cripit = ''
    lista = []
    vogais = []
    for i in range(0,len(frase)):

        if frase[i] == 'a' or frase[i] == 'e' or frase[i] == 'i'\
        or frase[i] == 'o' or frase[i] == 'u':
           cripit +=str('')
           vogais.append(str(frase[i]))
           lista.append(i)
           
        else:
            cripit +=str(frase[i])
            lista.append(i)
    
    descriptografa = ''

    for i in lista:

        descriptografa += str(frase[i])

    print(f'{cripit}')
    enter = input('Aperte enter...')
    print(f'{descriptografa}')

main()
