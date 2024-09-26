from ulid import ULID
import bancoDados as bancoDados
import os


def showListFilter(itens,data):
     for i in itens:
        print(f'''INDEX:[{i}] \nID: {data[i]["id"]}
NOME: {data[i]["nome"]}
PAÍS: {data[i]["pais"]}
ANO DE FUNDAÇÃO: {data[i]["anofundacao"]}\n''')
        

def isString(item,montadora):
    verificacao = True
    for i in range(len(item)):
        if not(item[i] == montadora[i]):
            verificacao = False

    return verificacao
        

def filtro(item,key,array):
    data = array
    newData = []
    for i in range(len(data)):
        if isString(item,data[i][key]):
            newData.append(i)

    return newData


def remove(index):
    montadoras = bancoDados.montadoras
    montadoras.pop(index)


def alteration(index):
    attribute = key(subMenuMontadoralistar())
    montadora = bancoDados.montadoras[index]

    if attribute == "nome":
        newName = input("Qual o novo nome da montadora: ")
        montadora[attribute] = newName
    elif attribute == "pais":
        newCountry = input("Qual o novo país da montadora: ")
        montadora[attribute] = newCountry
    elif attribute == "anofundacao":
        newYear = int(input("Digite o ano de fundação atualizado: "))
        montadora[attribute] = newYear


def showListar(lista):
    for i in range(len(lista)):
        print(f'''INDEX:[{i}] \nID: {lista[i]["id"]}
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
            id = ULID()
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
            opcao = int(input("Digite o index da montadora que você deseja alterar: "))
            alteration(opcao)
            clear()
            enter()
            clear()
        elif data == 4:#Remover valores da listar
            showListar(bancoDados.montadoras)
            opcao = int(input("Digite o index da montadora que deseja remover: "))
            remove(opcao)
            clear()
            print("Item removido da lista \n")
            enter()
            clear()
        elif data == 5:#Filtrar itens da listar
            keyData = key(subMenuMontadoralfilter())
            pesquisar = input("Buscar: ")
            filtrando = filtro(pesquisar,keyData,bancoDados.montadoras)
            showListFilter(filtrando,bancoDados.montadoras)
            enter()
            clear()
        elif data == 6:#Mostrar quantos itens estão dentro da listar
            qtdDados = len(bancoDados.montadoras)
            print(f''' ----- QUANTIDADE DE MONTADORAS -----
                  MONTADORAS: {qtdDados} \n''')
            enter()
            clear()
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

def subMenuMontadoralfilter():
    menu = f''' ----- MENU(FILTRAR) -----
    [1] - Nome
    [2] - País \n'''
    print(menu)
    opcao = int(input("Qual modo você deseja listar as montadoras: "))

    return opcao