import re

def main():

    text = str(input('Lista de palavras(,): '))
    palavras = re.split("[, . -]",text)
    contador = len(palavras)
    
    print(f'Quantidade de palavras:{contador}')

main()
