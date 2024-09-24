import bancoDados as bancoDados
import os

def showListar(lista):
    for i in range(len(lista)):
        print(f'''[{i}] ID: {lista[i]["id"]}
NOME: {lista[i]["nome"]}
PAÍS: {lista[i]["pais"]}
ANO DE FUNDAÇÃO: {lista[i]["anofundacao"]}\n''')
        

def bubbleSort(lista,ordem,variavel):
    tamanhoLista = len(lista)

    for i in range(tamanhoLista):
        for j in range(0,tamanhoLista-i-1):
            if ordem == "A":
                if lista[j][variavel] > lista[j+1][variavel]:
                    lista[j], lista[j+1] = lista[j+1], lista[j]
            elif ordem == "D":
                if lista[j][variavel] < lista[j+1][variavel]:
                    lista[j], lista[j+1] = lista[j+1], lista[j]

    return lista

#Função responsável por ordenar os dados
def ordenando(modo,func,ordem,listar):
    return func(listar,ordem,modo)
      
#Função responsável por apenas receber um input
def enter():
    return input("APERTE ENTER PARA CONTINUAR...")

#Função responsável por limpar a tela
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def entrada(text):

    dado = list(map(int,input(text).split(" ")))
    return dado[0]


def key(modo):
    if modo == 1:
        return "nome"
    elif modo == 2:
        return "pais"
    elif modo == 3:
        return "anofundacao"


def opcoes_Motadora(data):
   
   while data!= 0:
        #Cadastrando os dados das montadoras
        if data == 1:
            id = 0
            name = str(input("Digite o nome da montadora: "))
            pais= str(input("Digite o país da montadora: "))
            ano_Fundacao = int(input('Digite o ano de fundação: '))
            bancoDados.dadosMontadora([id,name,pais,ano_Fundacao],bancoDados.montadoras)
            clear()
            enter()
            clear()
        elif data == 2: #Listando as montadoras
            modo = subMenuMontadoralistar()
            ordem = str(input("Qual a forma qur você deseja listar as montadoras(A- Cresente, D- Decrecente): ")).upper()
            elementos_ordenados = ordenando(key(modo),bubbleSort,ordem,bancoDados.montadoras)
            clear()
            showListar(bancoDados.montadoras)
            enter()
            clear()
        elif data == 3:#Atualizar dados existentes
            showListar(bancoDados.montadoras)
            opcao = int(in)
        elif data == 4:#Remover valores da listar
            showListar(bancoDados.montadoras)
        elif data == 5:#Filtrar itens da listar
            pass
        elif data == 6:#Mostrar quantos itens estão dentro da listar
            qtdDados = len(bancoDados.montadoras)
            print(f''' ----- QUANTIDADE DE MONTADORAS -----
                  MONTADORAS: {qtdDados}''')
        data = menu_Montadora()
          

def menu_Montadora():
    menuMontadora = f''' ----- MENU(MONTADORA) -----
    1- Criar
    2- Listar todos
    3- Atualizar
    4- Remover
    5- Filtrar
    6- Status
    0- Sair \n'''
    print(menuMontadora)
    opcao = entrada("Digite qual opção que deseja: ")
    clear()

    return opcao


def subMenuMontadoralistar():
    menu = f''' ----- MENU(FILTRAR) -----
    [1] - Nome
    [2] - País
    [3] - Ano de fundação\n'''
    print(menu)
    opcao = int(input("Qual modo você deseja listar as montadoras: "))

    return opcao