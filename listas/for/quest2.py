def main():

    variavel = int(input('Digite ate que numero você deseja descobrir: '))

    for numero in range(1,variavel+1):
        if numero % 2 == 0:
            print(f'{numero}')

main()
