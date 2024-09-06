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
        data = list(map(int,input("Digite a opção: ").split(" ")))


main()