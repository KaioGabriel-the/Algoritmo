def main():

    frase = (str(input('Digite uma frase: '))).lower()
    quebrar = frase.split(" ")

    for i in range(0,len(quebrar)):
        print(f'{quebrar[i]}')

main()