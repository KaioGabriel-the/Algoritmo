def main():

    numero_identificacao = int(input('Digite o numero de identoficacao: '))
    peso = int(input('Peso: '))

    maior_i = 0
    maior_p = peso
    menor_i = 0
    menor_p = peso

    while numero_identificacao != 0:
        
        if peso > maior_p:
            maior_p = peso
            maior_i = numero_identificacao
        elif peso < menor_p:
            menor_p = peso
            menor_i = numero_identificacao
            
        numero_identificacao = int(input('Digite o numero de intetificacao: '))
        if numero_identificacao == 0:
            print(f'{resultado}')
        peso = int(input('Peso: '))

    resultado = print (f'Magro - id:{menor_i} peso:{menor_p}  Gordo - id:{maior_i} peso:{maior_p}')
    print(f'{resultado}')

main()

        