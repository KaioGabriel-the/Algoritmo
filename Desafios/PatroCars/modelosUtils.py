from ulid import ULID
import utils as utils
import bancoDados as bancoDados


def showModelos(datas,keys):
    for i in range(len(datas)):
        for j in range(len(datas[i])):
            print(f'''
            ID: {datas[i][j][keys[0]]}
            NOME DO MODELO: {datas[i][j][keys[1]]}
            ID MONTADORA: {datas[i][j][keys[2]]}
            VALOR REFERENCIAL: {datas[i][j][keys[3]]}
            MOTARIZAÇÃO: {datas[i][j][keys[4]]}
            TURBO: {datas[i][j][keys[5]]}
            AUTOMATICO: {datas[i][j][keys[6]]} \n''')


def trueFalse(string):
    return True if string == "S" else False


def opcoesFiltrarModelos(opcao):
    if opcao == 1:
        showModelos(bancoDados.modelosMontadoras,["id","nome","id_montadora","valor_referencial","motarizacao","turbo","automatico"])
    elif opcao == 2:
        print(f''' ----- LISTA DE MONTADORAS -----''')
        utils.showListar(bancoDados.montadoras)
        index = int(input("Digite o index da montadora: "))
        utils.clear()
        utils.enter()
        utils.clear()
        showModelos((bancoDados.modelosMontadoras[(bancoDados.whatMontadora(bancoDados.montadoras[index]["id"]))]),["id","nome","id_montadora","valor_referencial","motarizacao","turbo","automatico"])
        utils.enter()
        utils.clear()
    elif opcao == 3:
        pass
    elif opcao == 4:
        pass

def opcoesModelos(opcao):
    while opcao != 0:
        if opcao == 1:
            print(f''' ----- LISTA DE MONTADORAS -----''')
            utils.showListar(bancoDados.montadoras)
            data = int(input("Digite o index da montadora: "))
            utils.clear()
            utils.enter()
            utils.clear()
            id = ULID()
            nome = input("Digite o nome do modelo:")
            id_montadora = bancoDados.montadoras[data]["id"]
            valor_referencial = float(input("Digite o valor referencial: "))
            motarizacao = int(input("Digite a motarização: "))
            turbo = trueFalse(input("Tem turbo(S/N):").upper())
            automatico = trueFalse(input("É automatico(S/N): "))
            bancoDados.dadosModelos(id_montadora,[id,nome,id_montadora,valor_referencial,motarizacao,turbo,automatico])
            utils.clear()
            utils.enter()
            utils.clear()
        elif opcao == 2:
            modo = menuListarmodelo()
            utils.clear()
            opcoesFiltrarModelos(modo)
            utils.enter()
            utils.clear()
        elif opcao == 3:
            pass
            utils.clear()
        elif opcao == 4:
            pass
            utils.clear()
        opcao = menuModelos()
        utils.clear()


def menuListarmodelo():
    menu = f''' ----- MENU(FILTROS) -----
    1- LISTAR TODOS MODELOS
    2- LISTAR POR MONTADORA
    3- LISTAR TODOS OS MODELOS(SEM ATRIBUTOS)
    4- LISTAR LISTAR MEDELOS
    0- SAIR \n '''
    print(menu)
    opcao = int(input("Digite qual opção deseja: "))
    return opcao


def menuModelos():
    menu = f''' ----- MENU(MODELOS) ----- 
    1- ADICIONAR MODELO
    2- LISTAR MODELOS
    3- REMOVER MODELO
    4- EDITAR MODELO 
    0- SAIR \n'''
    print(menu)
    opcao = int(input("Digite qual opção deseja: "))
    return opcao