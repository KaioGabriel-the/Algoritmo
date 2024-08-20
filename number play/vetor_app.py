#Arquivo principal

#Importação da utils
import utils as input_data

#Função responsavel dizer qual o tipo de vetor
def filter001(option):

    if option == 1:

        size = input_data.input_manual("Qual o tamanho do vetor: ",0,10**10)
        min_max = input_data.input_split("Digite o minimo e o maximo(,): ")
        vector = 

    elif option == 2:

        size = input_data.input_manual("Qual o tamanho do vetor: ",0,10**10)
        min_max = input_data.input_split("Digite o minimo e o maximo(,): ")
        vector = input_data.building_vector(size,min_max)

    elif option == 3:
        pass
    elif option == 0:
        print(f'FIM DO PROBLEMA...')

def main():
    #entrada
    input_data.menu()

    option = filter001(input_data.input_manual("QUAL OPÇÃO: ",0,3))

main()