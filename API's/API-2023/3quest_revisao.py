def main():

    objetivo = str(input('Qual seu objetivo: '))
    quanto_objetivo = int(input('Qual o valor que é necessario para concluir seu objeivo: '))
    salario = float(input('Qual o valor do seu salario: '))
    porcentagem_salario = float(input('Quantos porcento deseja investir do seu salario(0.00): '))
    juros = float(input('Qual o valor do juros(0.00): '))

    investimento = salario * porcentagem_salario
    
    meses = 0
    valor_total = investimento

    while valor_total < quanto_objetivo:

        redimento = valor_total * juros * 1
        valor_total += redimento
        meses += 1

    anos = meses // 12
    qtd_meses = meses % 12

    print(f'Objetivo: {objetivo} \n Periodo para concluir: Anos - {anos} Meses - {qtd_meses}')

main()
    