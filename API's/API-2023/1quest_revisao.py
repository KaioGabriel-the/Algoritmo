def calcular_cash(valor):

    if valor <= 250:
        resultado = valor *0.05
        return resultado
    elif valor <= 500:
        resultado = valor *0.07
        return resultado
    elif valor <= 750:
        resultado = valor *0.08
        return resultado
    else:
        parte1 = 750 *0.08
        parte2 = valor - 750
        parte3 = parte2 * 0.25
        parte4 = parte1 + parte3
        return parte4

def main():

    nome = str(input('Nome: '))
    valor = float(input('Valor da comprar: '))
    programa = str(input('Você deseja finaliza program[S/N]: '))
    
    cash_total = 0
    rodadas_cash = 0
    valor_maior = 0
    valor_menor = 0
    valor_total = 0

    while programa != 'S':

        cash_total += calcular_cash(valor)
        rodadas_cash += 1
        valor_total += valor

        if valor < 0:
            if calcular_cash(valor)> valor_maior:
                valor_maior = calcular_cash(valor)
            elif calcular_cash(valor)< valor_menor:
                valor_menor = calcular_cash(valor)

        print(f'Nome:{nome} \n Cash: {calcular_cash(valor):.2f}')
        
        nome = str(input('Nome: '))
        valor = float(input('Valor da comprar: '))
        programa = str(input('Você deseja finaliza program[S/N]: '))



    faturamento = valor_total - cash_total
    media_cash = cash_total/rodadas_cash
    porcentagem = (cash_total/valor_total)*100

    print(f'Faturamento:{faturamento:.2f} \n Total de cash distribuido:{cash_total:.2f} \n Total de cash em reais: R$ {cash_total:.2f} \n Total de percentual em cash:{porcentagem:.2f} \n Maior valor em cash:{valor_maior} \n Menor valor rm cash:{valor_menor} \n Media do cash:{media_cash:.2f} ')
    
main()
