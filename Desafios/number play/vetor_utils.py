import utils as utils
import random

#Arquivo reponsável pelas funcionalidades de de vetor_funcinalidades

#Vai imprimir todos os elementos da lista
def print_vector(vector):
    element = 0

    for i in vector:
        print(f'{element}- elemento --> {i}')
        element += 1

#Vai retorna o tamanho do vetor
def size(vector):
    return len(vector)

#Vai resetar o vetor e padronizar os elementos
def patterning_vector(vector):
    vector_zero = [0] * size(vector)

    return vector_zero

#Retorna o menor e o maior lavor da lista e suas posicões
def position(vector):
    number_s = 0
    number_b = 0

    for i in range(size(vector)):
        if vector[i] < number_s:
            number_s = i
        elif vector[i] > number_b:
            number_b = i

    list_index = [number_s,number_b]

    return list_index

#Somar todos os elementos
def sum_element(vector):
    adding = 0

    for i in vector:
        adding += int(i)

    return adding

#Faz a média dos elementos do vetor
def average_vector(vector):
    average = sum_element(vector)/size(vector)

    return average

#Pegar todos os numeros positivos e a quantidade no vetor 
def numbers_positive_negative(vector,string):
    list_positive = []
    list_negative = []
    qtd_positive = 0
    qtd_negative = 0

    for i in vector:

        if i > 0:
            list_positive.append(i)
            qtd_positive += 1
        elif i < 0:
            list_negative.append(i)
            qtd_negative += 1

    if string == "p" :
        result = f'''{print_vector(list_positive)} /n - A QUANTIDADE DE NÚMEROS POSITIVOS É {qtd_positive}'''
        print(result)
    elif string == "n" :
        result = f'''{print_vector(list_negative)} /n - A QUANTIDADE DE NÚMEROS POSITIVOS É {qtd_negative}'''
        print(result)

#Irá multiplicar todos os números do vetor por um valor
def mult_numbers(vector,num):
    new_vector = []

    for i in vector:

        new_element = i * num
        new_vector.append(new_element)

    return new_vector

#Irá elevar todos os números do vetor a um valor
def ponteciacao_numbers(vector,num):
    new_vector = []

    for i in vector:

        new_element = i ** num
        new_vector.append(new_element)

    return new_vector

#Irá receber uma fração e multiplicar pelo elemento
def fracao_numbers(vector,numbers):
    new_vector = []
    fraction = numbers[0] / numbers[1]

    for i in vector:
        new_element = round((i * fraction),2) 
        new_vector.append(new_element)

    return new_vector

#Irá pegar todos os valores negativos e substituir aleatoriamente por valores de uma faixa
def substitui_negative(vector,min_max):
    new_vector = []

    for i in vector:

        if i < 0:
            new_element = random.randint(min_max[0],min_max[1])
            new_vector.append(new_element)
        else:
            new_vector.append(i)

    return new_vector

#Irá ordenar o valor os valores da lista em forma crescente
def ordena_numbers(vector):
    for i in range(len(vector)):
        for r in range(len(vector) - 1):
            if vector[r] > vector[r + 1]:
                maior = vector[r]
                vector[r] = vector[r + 1]
                vector[r + 1] = maior

    return vector

#Irá embaralhar os valores
def shuffle_numbers(vector):

    for i in range(len(vector)):
        vector[random.randint(0,len(vector)-1)] = vector[i]

    return vector

#Irá adicionar novos valores ao vetor
def add_numbers(vector):
    qtd = utils.number_min_max("Digite a quantidade de elementos que deseja remover: ",0,10*10)

    for i in range(qtd):
        number = utils.number_min_max("Qual o novo elemento que deseja adicionar no vetor: ",-10**11,10**10)
        vector.append(number)

    return vector

#Irá remover elementos do vetor por valor exato
def e_rem_numbers(vector):
    print_vector(vector)
    qtd = utils.number_min_max("Digite a quantidade de elementos que deseja remover: ",0,10*10)

    for i in range(qtd):
        element = int(input("Qual o elemento: "))
        vector.remove(element)

    return vector

#Irá remover elementos por indices
def i_rem_numbers(vector):
    print_vector(vector)
    qtd = utils.number_min_max("Digite a quantidade de elementos que deseja remover: ",0,10*10)

    for i in range(qtd):
        element = int(input("Qual a posição do elemento: "))
        vector.pop(element)

    return vector

#Irá editar valor especifico
def editar_numbers(vector):
    print_vector(vector)
    element = int(input("Qual o indice do elemento: "))
    new_element = utils.number_min_max("Digite o novo elemento: ",-10**11,10**10)
    vector[element] = new_element

    return vector