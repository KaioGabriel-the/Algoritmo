def main():

    lista = []
    y = lista.append(int(input('')))
    x = lista.append(int(input('')))
    z = lista.append(int(input('')))
    k = lista.append(int(input('')))
    a = lista.append(int(input('')))

    contador = 0

    for i in range(0,len(lista)):
        if int(lista[i]) % 2 == 0:
            contador += 1
    
    print(f'{contador} valores pares')

main()