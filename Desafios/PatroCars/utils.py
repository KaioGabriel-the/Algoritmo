import bancoDados as bancoDados
import os


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def entrada(text):

    dado = list(map(int,input(text).split(" ")))
    return dado[0]

def opcoes_Motadora(data):
    if data == 1:
        name = str(input("Digite o nome da montadora: "))
        paises = str(input("Digite o país da montadora: "))
        ano_Fundacao = int(input('Digite o ano de fundação: '))
        clear()
        print(f'Dado computado...')
        data = menu_Montadora()
    else:
        print(0)


def menu_Montadora():
    menuMontadora = f''' ----- MENU(MONTADORA) -----
    1- Criar
    2- Listar todos
    3- Atualizar
    4- Remover
    5- Filtrar
    0- Sair \n'''
    print(menuMontadora)
    opcao = entrada("Digite qual opção que deseja: ")

    return opcao