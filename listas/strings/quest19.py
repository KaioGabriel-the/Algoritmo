def transformar(numero):
    bits8 = numero // 10000000 ; bits7 = (numero % 10000000) // 1000000
    bits6 = ((numero % 10000000) % 1000000)// 100000 ; bits5 = (((numero % 10000000) % 1000000) % 100000) // 10000
    bits4 = ((((numero % 10000000) % 1000000) % 100000) % 10000)//1000 ; bits3 = (((((numero % 10000000) % 1000000) % 100000) % 10000)%1000) // 100
    bits2= ((((((numero % 10000000) % 1000000) % 100000) % 10000)%1000) % 100) // 10 ; bits1 = (((((((numero % 10000000) % 1000000) % 100000) % 10000)%1000) % 100) % 10) // 1

    resultado = (bits1)*1+(bits2)*2+(bits3)*4+(bits4)*8+(bits5)*16+(bits6)*32+(bits7)*64+(bits8)*128

    return resultado

def main():

    binario = str(input('Digite o numero binario:'))
    numero = int(binario)
    decimal = transformar(numero)
    print(f'Numero em decimal \n {decimal}')

main()