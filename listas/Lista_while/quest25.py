def main():

    numero_tv = int(input('Numero do canal: '))

    canal_2 = 0
    canal_4 = 0
    canal_7 = 0
    canal_10 = 0

    while numero_tv != 0:

        if numero_tv == 2:
            canal_2 += 1
        elif numero_tv == 4:
            canal_4 += 1
        elif numero_tv == 7:
            canal_7 += 1
        elif numero_tv == 10:
            canal_10 += 1
        
        numero_tv = int(input('Numero do canal: '))

    soma = canal_2 + canal_4 + canal_7 + canal_10
    porcentagem_2 = (canal_2 / soma) * 100
    porcentagem_4 = (canal_4 / soma) * 100
    porcentagem_7 = (canal_7 / soma) * 100
    porcentagem_10 = (canal_10 / soma) * 100

    print(f'Canal 2:{porcentagem_2} Canal 4:{porcentagem_4} Canal 7:{porcentagem_7} Canal 10:{porcentagem_10}')

main()

    
    
        