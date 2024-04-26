def main():

    limitesuprior = int(input('limite superior:'))

    for elemento in range(1,limitesuprior+1):
        if elemento**2 <= limitesuprior:
            resposta = elemento**2
        
    print(f'{resposta}')

main()