def juros_composto(juros,capital):

    montante = capital*(1*juros)**1

    return montante


def main():

    mes = int(input('Digite quando ira investir mensalmente: '))
    juros = float(input('Digite a taxa de juros: '))

    meses = 0
    capital = mes

    while  meses != 12:

     capital += juros_composto(juros,capital)
     adicionado += 100
     meses += 1
    print(f'Valor faturado:{capital}{main()}')

main()
