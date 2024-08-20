import random

#Arquivo responsável por entrada e saida de dados

#Menu responsável pela criação da lista
def menu():
    options = f"""  ----- MENU(DADOS) ----- \n
    0- ENCERRAR O PROGRAMA;
    1- CRIAR VETOR AUTOMÁTICO;
    2- INFORMA DADOS AO VETOR;
    3- CRIAR VETOR COM UM ARQUIVO;"""

    print(options)

#Criando vetor manualmente
def building_vector(size,min_max):
    
    new_vector = []

    for i in range(size):

        element = input("Digite o elemento do vetor: ",0,10*10)

        if element >= min_max[0] and element <= min_max[1]:
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
    return random.randint(int(min_max[0]),int(min_max[1]))
def input_split(text):

    data = (input()).split(",")

    new_data = []

    if int(data[0]) > 0 and int(data[1]) > int(data[0]):
        for i in data:
            new = int(data)
            new_data.append(new)
    elif int(data[0]) < 0:
        print(f'MINIMO MENOR QUE 0')
        input_split("DIGITE NOVAMENTE: ")
    elif int(data[1]) < int(data[0]):
        print(f'MAXIMO MENOR QUE O MINIMO')
        input_split("DIGITE NOVAMENTE: ")
    else:
        print(f'ERRO!!!')
        input_split("DIGITE NOVAMENTE: ")

    return new_data
               
def input_manual(text,min,mxm):

    data = int(input())

    if data < min and data <= mxm:
        return data
    else:
        return input_manual(text,min,mxm)