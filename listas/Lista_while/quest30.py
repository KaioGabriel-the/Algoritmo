def calcular_valor_final(valor_bruto,qtd):

    if qtd <= 10:
        final = valor_bruto
        return final
    elif qtd <= 20:
        desconto = valor_bruto * 0.1
        final = valor_bruto - desconto
        return final
    elif qtd <= 50:
        desconto = valor_bruto * 0.2
        final = valor_bruto - desconto
        return final
    elif qtd > 50 :
        desconto = valor_bruto * 0.25
        final = valor_bruto - desconto
        return final

def main():

    produto = str(input('DIGITE O NOME DO PRODUTO: '))
    preco = int(input('DIGITE O PREÇO DO PRODUTO: '))
    qtd = int(input('DIGITE A QUANTIDADE DE PRODUTOS: '))


    while produto != 'FIM':

        valor_bruto = qtd * preco
        valor_final = calcular_valor_final(valor_bruto,qtd)

        print(f'PRODUTO:{produto}  VALOR DA COMPRAR:{valor_final}')

        produto = str(input('DIGITE O NOME DO PRODUTO: ')).upper()
        if produto != 'FIM':
            preco = int(input('DIGITE O PREÇO DO PRODUTO: '))
            qtd = int(input('DIGITE A QUANTIDADE DE PRODUTOS: '))
        else:
            print('................')


main()