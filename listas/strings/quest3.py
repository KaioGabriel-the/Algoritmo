def main():

    frase = (str(input('Digite uma frase: '))).lower()
    quebrar = frase.split(" ")

    juntar = ''
    for i in range(0,len(quebrar)):
        juntar += str(quebrar[i])

    print(f'{juntar}')

main()