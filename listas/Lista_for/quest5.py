def main():

    numero = int(input('Digite o numero que deseja saber o fatorial: '))

    multiplicao = 1

    for elemento in range (1,numero+1):

        multiplicao = multiplicao * elemento

    print(f'{numero}! é igaul a {multiplicao}')        

main()