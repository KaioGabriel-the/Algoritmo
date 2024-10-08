import random

#Arquivo responsável por entrada e saida de dados

#Menu responsável pelos maps que os elementos dos vetores
def menu_rules():
    opctions = f''' ---> MENU(REGRAS) <--- \n
    1- MULTIPLICAR TODOS OS ELEMENTOS
    2- ELEVAR TODOS OS ELEMENTOS
    3- REDUZIR A UMA FRAÇÃO TODOS OS ELEMENTOS
    4- SUBSTITUIR OS VALORES NEGATIVOS POR UM NÚMERO ALEATORIO 
    5- ORDENAR VALORES DE FORMA CRESCENTE
    6- EMBARALHAR VALORES
    '''
    print(opctions)

#Menu_responsável pelas funcionalidades dos vetores
def menu_vector():
    opctions = f''' ---> MENU(VETOR) <--- \n
    1- MOSTRAR DOS OS ELEMENTOS DO VETOR;
    2- RESETAR O VETOR E PADRONIZAR COM UM VALOR;
    3- VER QUANTIDADE DE ELEMENTO NA LISTA;
    4- VER MENOR E MAIOR VALOR DA LISTA E SUAS POSIÇÕES;
    5- SOMATÓRIO DOS VALORES;
    6- MÉDIA DOS VALORES;
    7- MOSTRAR TODOS OS VALORES POSITIVOS E A QUANTIDADE;
    8- MOSTRAR TODOS OS VALORES NEGATIVOS E A QUANTIDADE;
    9- ATUALIZAR OS VALORES ATRAVEIS DE UMA DAS REGRA;
    10- ADICIONAR VALORES;
    11- REMOVER ITENS POR NÚMERO EXATO;
    12- REMOVER POR POSIÇÃO;
    13- EDITAR ITEM POR POSIÇÃO;
    14- SALVAR VALORES EM UM ARQUIVO;
    0 - SAIR(SALVAMENTO AUTOMÁTICO);
    '''
    print(opctions)

#Menu responsável pela criação da lista
def menu():
    options = f"""  ----- MENU(DADOS) ----- \n
    1- CRIAR VETOR AUTOMÁTICO;
    2- INFORMA DADOS AO VETOR;
    3- CRIAR VETOR COM UM ARQUIVO; \n"""
    print(options)

    option = number_min_max("Digite qual opção deseja: ",0,3)

    return option

#Criando vetor manualmente
def building_vector(size,min_max):
    new_vector = []

    for i in range(size):

        element = number_min_max("Digite o elemento do vetor: ",0,10*10)

        if element >= (min_max[0]) and element <= (min_max[1]):
            new_vector.append(element)
        else:
            i = i

    return new_vector

#Criando vetor automático
def automstic_vector(size,min_max):
    new_list = []

    for i in range(size):

        new_list.append(get_random_number(min_max))

    return new_list


def get_random_number(min_max):
    return random.randint((min_max[0]),(min_max[1]))

#Leitor de arquivos
def file_scanner(name_file):
    new_vector = []

    with open(name_file,"r") as arquivo:

        linhas = arquivo.readline()

    for i in linhas:

        new_vector.append(int(i.strip()))

    return new_vector

#Pegar o min. e max.
def input_split(text):
    data = (input(text)).split(",")
    new_data = []

    if int(data[1]) > int(data[0]):
        for i in data:
            new = int(i)
            new_data.append(new)
    elif int(data[1]) < int(data[0]):
        print(f'MAXIMO MENOR QUE O MINIMO')
        input_split("DIGITE NOVAMENTE: ")
    else:
        print(f'ERRO!!!')
        input_split("DIGITE NOVAMENTE: ")

    return new_data


def number_min_max(text,min,mxm):
    data = int(input(text))

    if data > min and data <= mxm:
        return data
    else:
        return number_min_max(text,min,mxm)


def input_string(text):
    string = str(input(text))

    return string


def enter():
    press = input("Precione o enter...")

    return