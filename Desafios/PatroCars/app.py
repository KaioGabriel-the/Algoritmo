import utils as utils
import modelosUtils as modeloUtils

def main():
    menu = f''' ----- MENU ----- 
    1- Montadoras
    2- Modelos de Veículos
    3- Veículos
    0- Encerrar o programa \n'''
    print(menu)
    entrada = utils.entrada("Digite sua opção: ")
    utils.clear()

    while entrada != 0:
        if entrada == 1:
            opcao = utils.menu_Montadora()
            utils.opcoes_Motadora(opcao)
            utils.clear()
            print(menu)
            entrada = utils.entrada("Digite sua opção: ")
            utils.clear()
        elif entrada == 2:
            opcao = modeloUtils.menuModelos()
            utils.clear()
            modeloUtils.opcoesModelos(opcao)
            utils.clear()
            print(menu)
            entrada = utils.entrada("Digite sua opção: ")
            utils.clear()
        elif entrada == 3:
            pass


main()