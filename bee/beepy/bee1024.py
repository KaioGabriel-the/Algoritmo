#Pegar metade da string e soma mais um no code ascii

def verificacao3(code):
    metade = len(code) // 2
    new_string = ''

    for i in range(len(code)):

        if i < metade:
            new_string += code[i]
        else:
            index = chr(ord(code[i])- 1)
            new_string = new_string + index

    return new_string

#Invertir a string
def verificacao2(code):

    new_string = ''

    for i in range(len(code)):
        new_string = code[i] + new_string
    
    return new_string

#Verifica se é uma letra
def eh_letra(letra):

    if ord(letra) >= 65 and ord(letra) <= 90:
        return True
    elif ord(letra) >= 97 and ord(letra) <= 122:
        return True
    else:
        False

# Verifica se é letra maiuscular ou minuscular e deslocar 3 casas para direita na tabela ascii
def verificacao1(code):

    new_string = ''

    for i in range(len(code)):

        letra = code[i]

        if eh_letra(letra):

            new_string += chr(ord(letra) + 3)
        else:
            new_string += letra

    return new_string

def main():

    entrada = int(input())

    for i in range(entrada):
        #Entrada
        frase = input()

        #Processamento
        filter001 = verificacao1(frase)
        filter002 = verificacao2(filter001)
        filter003 = verificacao3(filter002)

        print(f'''{filter003}''')

main()