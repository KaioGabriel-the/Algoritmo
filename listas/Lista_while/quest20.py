def carro_parou(km_percorridos):

    if km_percorridos == 600:
        print(f'Concluiu seu percurso completo')
    elif km_percorridos > 600:
        print(f'Concluiu seu percursp,mas passou dos 600 km')
    else:
        print(f'Não concluiu')

def litros_parou(litros_gastos):
    if litros_gastos == 50:
        print(f'Todo cumbustivel usado')
    elif litros_gastos < 50:
        print(f'Ainda sobrou combustivel')

def main():

    quantos_km = int(input('Quantos km você percorreu: '))
    litros = int(input('Quantos litros de combustivel gastou:'))

    litros_gastos = 0
    km_percorridos = 0

    while litros_gastos != 50 or km_percorridos != 600:
        litros_gastos += litros
        km_percorridos += quantos_km

        quantos_km = int(input('Quantos km você percorreu: '))
        litros = int(input('Quantos litros de combustivel gastou:'))
    
    carro = carro_parou(km_percorridos)
    litros_1 = litros_parou(litros_gastos)
    l_km = litros_gastos/km_percorridos

    print(f'{carro} {litros_1} {l_km}')

main()
    



