import vetor_utils as utils
import utils as utils_data

#Arquivo responsável pelas funcionalidades que seram chamadas na vetor app

#Mostrar vetores
def vector_show(vector):

    return utils.print_vector(vector)

#Mostrar a quantidade de valores no vetor
def vector_amount(vector):
    
    result = f'''A QUANTIDADE DE ELEMENTOS É {utils.size(vector)}'''
    return result

#Resetar o vetor e padroniza todos os elementos
def reset_vector(vector):

    number = utils_data.input_manual("Digite o valor padrão da lista: ",0,10*10)
    
    return utils.patterning_vector(vector,number)

#Retornará um maior e menor valor do vetor e suas posições
def smaller_bigger(vector):
    list_index = utils.position(vector)

    result = f''' - MENOR: {vector[list_index[0]]} - POSIÇÃO: {list_index[0]} \n - MAIOR: {vector[list_index[1]]} - POSIÇÃO: {list_index[1]}'''

    print(result)

#Retorna a soma de todos os elementos do vetor
def sum(vector):
    
    result = f'''A SOMA DOS ELEMENTOS DO VETOR É {utils.sum_element(vector)}'''

    return result

#Retorna a média dos elementos do vetor
def average(vector):

    result = f'''A MÉDIA ENTRE OS VALORES É {utils.average_vector(vector)}'''

    return result

#Retorna todos os numeros positivos e a quantidade que o vetor possui
def positive_negative(vector,string):
    return utils.numbers_positive_negative(vector,string)

#Retorna todos os valores do vetor multiplicados por um valor
def mult(vector):

    number = utils_data.input_manual("Digite o número: ",0,10*10)
    new_vector = utils.mult_numbers(vector,number)

    return new_vector

#Retorna todos os elementos do vetor elevados a um valor
def pon(vector):

    number = utils_data.input_manual("Digite o número: ",0,10*10)
    new_vector = utils.pon_numbers(vector,number)

    return new_vector

#Retorna todos os elementos transformados por uma fração
def frac(vector):

    number = (str(input("Digite a fração(1/2): "))).split("/")
    new_vector = utils.fra_numbers(vector,number)

    return new_vector

#Substitui todos os valores negativos do vetor
def subst_negative(vector):

    number = utils_data.input_split("Digite o minimo e o maximo(,): ")
    new_vector = utils.sub_negative(vector,number)

    return new_vector

#Ordenar os números do menor para o maior
def ord_vector(vector):

    new_vector = utils.ord_numbers(vector)

    return new_vector

#Embaralharar os elementos