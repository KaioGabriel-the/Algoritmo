def string20(text):
    x = str(input(text))

    if len(x) <= 20:
        return x
    else:
        print(f'Passou do limite!!!')
        x = string20(text)

def colunas(n,text):

    for i in range (0,len(text)):
        v = ''
        for x in range(0,n-1):
            v += str(' ')
            x+=1
        print(f'{v + text[i]}')
        i += 1
    
    return ''

def main():

    string = string20('Digite sua sting:')
    coluna = int(input('Digite a coluna:'))

    print(f'------------------------------')
    print(f'{colunas(10,string)}')

main()