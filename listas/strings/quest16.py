def string20(text):
    x = str(input(text))

    if len(x) <= 20:
        return x
    else:
        print(f'Passou do limite!!!')
        x = string20(text)

def diagonal(text):

    for i in range (0,len(text)):
       print(f'{i*' ' + text[i]}')
    
    return ''

def main():

    string = string20('Digite sua sting:')
    print(f'{diagonal(string)}')

main()