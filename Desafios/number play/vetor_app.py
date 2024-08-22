#Arquivo principal

#Importação da vetor funcionalidades
import vetor_funcionalidades as utils_vector
#Importação da utils
import utils as input_data

#Função respnsavel por chamar as funcionalidades dos vetores
def filter002(vector):

    input_data.menu_vector()

    opction = input_data.input_manual("Digite qual opção deseja: ",0,14)

    current_vector = vector

    while opction != 0 and opction <= 14:

        #Responsável por mostrar os dados do vetor
        if opction == 1:
            current_vector = utils_vector.vector_show(current_vector)

            input_data.menu_vector()

            opction = input_data.input_manual("Digite qual opção deseja: ",0,14)
        #Responsável por resetar o vetor e padronizar um valor em todos os elementos
        elif opction == 2:
            current_vector = utils_vector.reset_vector(vector)

            input_data.menu_vector()

            opction = input_data.input_manual("Digite qual opção deseja: ",0,14)
        #Reponsável por dizer a quantidade de elementos do vetor
        elif opction == 3:
            current_vector = utils_vector.vector_amount(current_vector)

            input_data.menu_vector()

            opction = input_data.input_manual("Digite qual opção deseja: ",0,14)
        #Responsável por mostrar o menor e o maior valor e suas respectiva posições do vetor
        elif opction == 4:
            current_vector = utils_vector.smaller_bigger(current_vector)

            input_data.menu_vector()

            opction = input_data.input_manual("Digite qual opção deseja: ",0,14)
        #Responável por somar todos os elementos dos vetor
        elif opction == 5:
            current_vector = utils_vector.sum(current_vector)

            input_data.menu_vector()

            opction = input_data.input_manual("Digite qual opção deseja: ",0,14) 
        #Responsável por fazer a média dos elementos do vetor
        elif opction == 6:
            current_vector = utils_vector.average(current_vector)

            input_data.menu_vector()

            opction = input_data.input_manual("Digite qual opção deseja: ",0,14)
        #Responsável por pegar todos os números positivos e a quantidades no vetor
        elif opction == 7:
            current_vector = utils_vector.positive_negative(current_vector,"p")

            input_data.menu_vector()

            opction = input_data.input_manual("Digite qual opção deseja: ",0,14)
        #Responsável por pegar todos os números negativos e a quantidade no vetor
        elif opction == 8:
            current_vector = utils_vector.positive_negative(current_vector,"n")

            input_data.menu_vector()

            opction = input_data.input_manual("Digite qual opção deseja: ",0,14)

        

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

#Função principais
def main():

    opction = input_data.menu()
    set_vector = filter001(opction)
    vector_features = filter002(set_vector)
    print(f'FIM DO PROGRAMA!!!')
main()