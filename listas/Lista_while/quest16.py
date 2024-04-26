def main():

    valor_divida = int(input('Digite o valor do seu emprestimo: '))
    valor_diario = int(input('Digite o valor que você pagar diariamente: '))

    valor_divida_a = valor_divida
    volor_diario_b = valor_diario
    qtd_dias = 0

    while valor_divida_a != volor_diario_b:
        novo_valor = valor_divida_a - valor_diario
        valor_divida = novo_valor *0.0085
        valor_diario += 200
        qtd_dias += 1

    print(f'Quantidades de dias que serão necessarios para pagar o emprestimo: {qtd_dias}')
    
main()
