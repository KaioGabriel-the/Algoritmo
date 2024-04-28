def main():

    frase = str(input('Digite uma frase: ')).lower()

    for i in range(0,len(frase)):
        if frase[i] == 'a' or frase[i] == 'e' or frase[i] == 'i'\
        or frase[i] == 'o' or frase[i] == 'u'or frase[i] == " ":
         print (f'{frase[i]}')
        else:
           print(f'#')
        i += 1

main()