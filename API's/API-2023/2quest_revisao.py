def calcular_resto(limite):

    if limite % 1000 !=0:
        resto = limite % 1000
        return resto
    else:
        resto = 0
        return resto
    
def calcular_conta(preco,limite):
    resultado = limite // 1000
    resto = calcular_resto(limite)
    conta = (resultado + resto)*preco
    return conta
        

def main():
    largura = int(input('Largura(cm³): '))
    comprimento = int(input('Comprimento(cm³): '))
    profundidade = int(input('Profundidade(cm³): '))
    preco = float(input('Quanto é cobrado por 1000 litros de água: '))

    capacidade = (largura * comprimento * profundidade)/1000 
    limite = capacidade - capacidade*0.15
    valor_conta = calcular_conta(preco,limite)
    reposicao = limite * 0.1
    preco_reposicao = calcular_conta(preco,reposicao)

    print(f'Capacidade maxima:{capacidade:2} \n Quantidade que é recomendado a encher:{limite:.2} \n Preço que deverá pagar para encher a piscina:{valor_conta:.2f} \n Quantidade de água que precisa ser reposta mensalmente:{reposicao:.2f} \n Valor que pagará pela reposição:{preco_reposicao:2f}')

main()
