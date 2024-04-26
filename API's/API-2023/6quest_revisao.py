def calcular_pis(qtd_kwh):
    if qtd_kwh <= 30:
        return 0
    elif qtd_kwh <= 100:
        parte3 = (qtd_kwh * 0.59)*0.15
        return parte3
    elif qtd_kwh > 100:
        parte3 = (qtd_kwh * 0.75)*0.15
        return parte3   

def calcular_icms(qtd_kwh):
    if qtd_kwh <= 30:
        return 0
    elif qtd_kwh <= 100:
        parte2 = (qtd_kwh * 0.59)*0.25
        return parte2
    elif qtd_kwh > 100:
        parte2 = (qtd_kwh * 0.75)*0.25
        return parte2

def tarifa_iluminacao(qtd_kwh):
    if qtd_kwh <= 80:
        return 0
    elif qtd_kwh > 80 and qtd_kwh <= 100:
        resultado = qtd_kwh * 0.59*0.06
        return resultado
    else:
        resultado = qtd_kwh * 0.75*0.06
        return resultado


def calcular_kwh(qtd_kwh):

    if qtd_kwh <= 30:
        return 0
    elif qtd_kwh > 30 and qtd_kwh <=100:
        if  qtd_kwh > 80 :
            parte1 = (qtd_kwh * 0.59*0.06) + qtd_kwh * 0.59
            parte2 = (qtd_kwh * 0.59)*0.25
            parte3 = (qtd_kwh * 0.59)*0.15
            resultado = parte1 + parte2 + parte3
            return resultado
        elif qtd_kwh <= 80:
           parte1 = qtd_kwh * 0.59
           parte2 = (qtd_kwh * 0.59)*0.25
           parte3 = (qtd_kwh * 0.59)*0.15
           resultado = parte1 + parte2 + parte3
           return resultado
    elif qtd_kwh >100:
        parte1 = (qtd_kwh * 0.75*0.06) + qtd_kwh * 0.75
        parte2 = (qtd_kwh * 0.75)*0.25
        parte3 = (qtd_kwh * 0.75)*0.15
        resultado = parte1 + parte2 + parte3
        return resultado

def main():
    leitura_atul = int(input('Leitura atual: '))
    leitura_anterior = int(input('Leitura anterior: '))

    qtd_kwh = leitura_atul - leitura_anterior
    valor_kwh = calcular_kwh(qtd_kwh)
    iluminacao = tarifa_iluminacao(qtd_kwh)
    icms = calcular_icms(qtd_kwh)
    pis = calcular_pis(qtd_kwh)
    tarifa = (qtd_kwh // 100) *8
    valor_pagar = valor_kwh + tarifa
    print(f'Consumo {qtd_kwh} KWh \n Valor Faturado R$ {valor_pagar:.2f} \n Bandeira R$ 8,00 (bandeira vermelha) \n ICMS R$ {icms:.2f} \n PIS/CONFIS R$ {pis:.2f} \n Taxa Iluminação R$ {iluminacao:.2f}')

main()
