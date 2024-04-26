def cdu(variavel,numero):

    if variavel == 'c':
        return numero // 100
    elif variavel == 'd':
        return (numero % 100) // 10
    elif variavel == 'u':
        return (numero % 100) % 10

def calcular_unidade_romano(unidade):

    if unidade == 1:
        return 'I'
    elif unidade == 2:
        return 'II'
    elif unidade == 3:
        return 'III'
    elif unidade == 4:
        return 'IV'
    elif unidade == 5:
        return 'V'
    elif unidade == 6:
        return 'VI'
    elif unidade == 7:
        return 'VII'
    elif unidade == 8:
        return 'VIII'
    elif unidade == 9:
        return 'IX'

def calcular_dezena_romano(dezena):
    if dezena == 10:
        return 'X'
    elif dezena == 2:
        return 'XX'
    elif dezena == 3:
        return 'XXX'
    elif dezena == 4:
        return 'XL'
    elif dezena == 5:
        return 'L'
    elif dezena == 6:
        return 'LX'
    elif dezena == 7:
        return 'LXX'
    elif dezena == 8:
        return 'LXXX'
    elif dezena == 9:
        return 'XC'

def calcular_centena_romano(centena):

    if centena == 100:
        return 'C'
    elif centena == 200:
        return 'CC'
    elif centena == 300:
        return 'CCC'
    elif centena == 400:
        return 'CD'
    elif centena == 500:
        return 'D'
    elif centena == 600:
        return 'DC'
    elif centena == 700:
        return 'DCC'
    elif centena == 800:
        return 'DCC'
    elif centena == 900:
        return 'MC'


def main():

    numero = int(input('DIGITE UM NUMERO(1 até 999):'))

    while numero > 0:

        if numero == 0:
            return '0'
        elif numero > 0:
            unidade = cdu('u',numero)
            dezena = cdu('d',numero)
            centena = cdu('c',numero)

            unidade_romano = calcular_unidade_romano(unidade)
            dezena_romano = calcular_dezena_romano(dezena)
            centena_romano = calcular_centena_romano(centena)

            soma = str(centena_romano) + str(dezena_romano) + str(unidade_romano)
            print(f'O numero {numero} e em romano {soma}')

            numero = int(input('DIGITE OUTRO NUMERO:'))

main()
  