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
def patterning_vector(vector,number):

    vector_zero = [0] * size(vector)
    new_vector = [number] * size(vector_zero)

    return new_vector

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