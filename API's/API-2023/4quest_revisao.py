def aceito_nao_emprestimo(quarenta_renda,valor_parcelas):

    if valor_parcelas > quarenta_renda:
        print(f'Emprestimo negado')
    else:
        print(f'Emprestimo aceito')

def calcular_ifo(parcelas,emprestimo):
    dias = 30 * parcelas
    parte1 = emprestimo * 0.0038
    
    flag = 0
    parte = 0

    while flag != dias:
        resultado = emprestimo *0.000082
        parte += resultado
        flag += 1
    
    soma = parte1 + parte
    return soma
        
def calcular_parcelas(valor,parcelas):
    
    if parcelas < 2:
        return 0
    elif parcelas <=6 :
        montante = valor * (1*(0.1375/2))^1
        return montante
    elif parcelas <= 12 :
        montante = valor * (1*(0.1375*0.75))^1
        return montante
    elif parcelas <= 18 :
        montante = valor * (1*(0.1375*1))^1
        return montante
    elif parcelas <= 24 :
        montante = valor * (1*(0.1375*1.3))^1
        return montante
    else:
        return 0

def get_number_in_range(mensagem, min, max):
  numero = int(input(mensagem))

  if (numero < min or numero > max):
        print('Número inválido! Digite novamente')
        return get_number_in_range(mensagem, min, max)
    

  return numero


def main():
    #entrada
    renda_mensal = float(input('Qual sua resnda mensal: '))
    valor_empresimo = get_number_in_range('Qual o valor do emprestimo que deseja: ',1200,100000)
    parcelas = get_number_in_range('Em quantas parcela deseja pagar: ',2,24)
    
    #processamento
    ifo = calcular_ifo(parcelas,valor_empresimo)
    valor = valor_empresimo + ifo

    qtd_parcelas = 0
    valor_pagar = valor

    while qtd_parcelas != parcelas:

        conta = calcular_parcelas(valor_pagar,parcelas)
        valor_pagar += conta
        qtd_parcelas += 1

    quarenta_renda = renda_mensal *0.4
    valor_parcelas = valor_pagar // parcelas
    porcentagem = (renda_mensal / valor_parcelas)*100
    porcentagem_juros = ((valor_pagar - valor_empresimo)/valor_empresimo)*100

    aceito_nao = aceito_nao_emprestimo(quarenta_renda,valor_parcelas)

    print(f'Valor Pedido:{valor_empresimo} \n Valor do IOF:{ifo} \n Valor dos Juros a pagar:{porcentagem_juros}  \n Valor Total a pagar: R$ {valor_pagar} \n Valor da Parcela Mensal: {parcelas}x de R$ {valor_parcelas} \n Comprometimento da Renda Mensal (%):{porcentagem} \n Se Empréstimo APROVADO ou NEGADO:{aceito_nao}')
              
main()