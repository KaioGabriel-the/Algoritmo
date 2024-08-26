import vetor_utils as utils
import utils as utils_data

#Arquivo responteciacaosável pelas funcionalidades que seram chamadas na vetor app
#Mostrar vetores
def vector_show(vector):
    return utils.print_vector(vector)

#Mostrar a quantidade de valores no vetor
def vector_amount(vector):
    result = f'''A QUANTIDADE DE ELEMENTOS É {utils.size(vector)}'''
    return result

#Resetar o vetor e padroniza todos os elementos
def reset_vector(vector):
    number = utils_data.number_min_max("Digite o valor padrão da lista: ",0,10*10)
    return utils.patterning_vector(vector)

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
def multiplicacao(vector):
    number = utils_data.number_min_max("Digite o número: ",0,10*10)
    new_vector = utils.mult_numbers(vector,number)

    return new_vector

#Retorna todos os elementos do vetor elevados a um valor
def ponteciacao(vector):
    number = utils_data.number_min_max("Digite o número: ",0,10*10)
    new_vector = utils.ponteciacao_numbers(vector,number)

    return new_vector

#Retorna todos os elementos transformados por uma fração
def fracao(vector):
    number = (str(input("Digite a fração(1/2): "))).split("/")
    new_vector = utils.ponteciacao_numbers(vector,number)

    return new_vector

#Substitui todos os valores negativos do vetor
def substitui_numbers_negative(vector):
    number = utils_data.input_split("Digite o minimo e o maximo(,): ")
    new_vector = utils.substitui_negative(vector,number)

    return new_vector

#Ordenar os números do menor para o maior
def ordena_vector(vector):
    new_vector = utils.ordena_numbers(vector)

    return new_vector

#Embaralharar os elementos
def shuffle(vector):
    new_vector = utils.shuffle_numbers(vector)

    return new_vector

#Adicionar novos valores ao vetor
def add(vector):
    utils.add_numbers(vector)

#Removerá elementos do vetor atraveis do valor exato
def remove(vector):
    return utils.e_rem_numbers(vector)

#Removerá os elementos do vetores por indice
def remove_index(vector):
    return utils.i_rem_numbers(vector)

#Editar elementos
def editar_vector(vector):
    return utils.editar_numbers(vector)

#Criar arquivo com os elementos do vetor
def create_file(vector,name):
    file = f"{name}.txt"

    with open(file,'w') as arquivo:

        for numbers in vector:
            arquivo.write(f"{numbers}\n")