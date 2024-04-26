def calcular_populacao(variavel,cidade):
    if variavel == 'a':
        crescimento = cidade * 0.035
        populacao_nova = cidade + crescimento
        return populacao_nova
    elif variavel == 'b':
        crescimento = cidade * 0.0135
        populacao_nova = cidade + crescimento
        return populacao_nova

def main():

    cidade_a = int(input('Digite o numero de habitantes da cidade A: '))
    cidade_b = int(input('Digite o numero de habitantes da cidade B: '))

    cidade_aa = cidade_a
    cidade_bb = cidade_b
    anos = 0

    while cidade_aa != cidade_bb:
        populacao_a = calcular_populacao('a',cidade_aa)
        populacao_b = calcular_populacao('b',cidade_bb)

        cidade_aa += populacao_a
        cidade_bb += populacao_b
        anos += 1
    print(f'Os anos necessarios para cidade a ter a mesma população que a cidade b é {anos} ')

main()