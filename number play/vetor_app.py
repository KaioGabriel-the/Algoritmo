#Arquivo principal

#Iportação da vetor funcionalidades
import vetor_funcionalidades as utils_vector
#Importação da utils
import utils as input_data

#Função respnsavel por chamar as funcionalidades dos vetores
def filter002(vector):

    input_data.menu_vector()

    opction = input_data.input_manual("Digite qual opção deseja: ",0,14)

    current_vector = vector

    while opction != 0 and opction <= 14:

        #Responsável por mostrar os dados da lista
        if opction == 1:
            current_vector = utils_vector.vector_show(current_vector)

            input_data.menu_vector()

            opction = input_data.input_manual("Digite qual opção deseja: ",0,14)
        #Responsável por resetar o vetor e padronizar um valor em todos os elementos
        elif opction == 2:
            current_vector = utils_vector.reset_vector(vector)

            input_data.menu_vector()

            opction = input_data.input_manual("Digite qual opção deseja: ",0,14)
        #Reponsável por dizer a quantidade de elementos
        elif opction == 3:
            current_vector = utils_vector.vector_amount(current_vector)

            input_data.menu_vector()

            opction = input_data.input_manual("Digite qual opção deseja: ",0,14)
        #Responsável por mostrar o menor e o maior valor e suas respectiva posições
        elif opction == 4:
            pass
#Função responsavel dizer qual o tipo de vetor
def filter001(option):

    #Responsável por criar um vetor automatico
    if option == 1:

        size = input_data.input_manual("Qual o tamanho do vetor: ",0,10**10)
        min_max = input_data.input_split("Digite o minimo e o maximo(,): ")
        vector = input_data.automstic_vector(size,min_max)
        return vector
    #Responsável por criar um vetor manual
    elif option == 2:

        size = input_data.input_manual("Qual o tamanho do vetor: ",0,10**10)
        min_max = input_data.input_split("Digite o minimo e o maximo(,): ")
        vector = input_data.building_vector(size,min_max)
        return vector
    #Responável por criar um vetor atraveis de um arquivo
    elif option == 3:
        fin = input_data.input_string("Passe o arquivo: ")
        vector = input_data.file_scanner(fin)
        return vector

def main():

    opction = input_data.menu()
    set_vector = filter001(opction)
    vector_features = filter002(set_vector)
    print(f'FIM DO PROGRAMA!!!')
main()