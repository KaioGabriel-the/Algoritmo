def fatorial(entrada):
    result = 1

    for i in range(entrada):
        result = result * entrada - i


def main():
    menu = f"""----- MENU -----
    1- FATORIAL
    2- SEQUÊCIA DE FIBONACCI
    3-  SEQUÊCIA SIMPLES
    4 - PRODUTO DA MULTIPLICAÇÃO
    5 - POTÊNCIA
    6 -  SOMA ALEATÓRIA
    7 - CONTAR VOGAIS E CONSOANTES
    8 - GRAVAR EM ARQUIVO \n"""
    print(menu)
    data = list(map(int,input("Digite a opção: ").split(" ")))

    while data[0] != 0:
        if data[0] == 1:
            entrada = int(input("Digite fatorial: "))
            result = fatorial(entrada)
            print(f"""> O fatorial é {result}""")
        data = list(map(int,input("Digite a opção: ").split(" ")))


main()