import vetor_utils as utils
import utils as utils_data

#Arquivo responsável pelas funcionalidades que seram chamadas na vetor app

#Mostrar vetores
def vector_show(vector):

    return utils.print_vector(vector)

#Mostrar a quantidade de valores no vetor
def vector_amount(vector):

    return utils.size(vector)

#Resetar o vetor e padroniza todos os elementos
def reset_vector(vector):

    number = utils_data.input_manual("Digite o valor padrão da lista: ",0,10*10)
    
    return utils.patterning_vector(vector,number)

#Retornará um maior e menor valor do vetor e suas posições
def smaller_bigger(vector):
    list_index = utils.position(vector)

    result = f''' - MENOR: {vector[list_index[0]]} - POSIÇÃO: {list_index[0]} \n - MAIOR: {vector[list_index[1]]} - POSIÇÃO: {list_index[1]}'''

    print(result)

def sum_elements(vector):
    pass