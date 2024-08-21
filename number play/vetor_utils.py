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