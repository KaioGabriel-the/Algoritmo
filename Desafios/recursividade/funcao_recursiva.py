def gravar_Arquivo(name,dados):
    with open(f"{name+".txt"}","w") as file:
        for i in dados:
            file.write(f"{i}\n")

    file.close()

def fibonacci(comprimento):
    pass 


def fatorial(elemento):
    if elemento <= 1:
        return 1
        
    return elemento * fatorial(elemento-1)


def main():
    arquivo = f"----- GRAVAR EM ARQUIVO -----"
    print(arquivo)
    name_File = str(input("Digite o nome do arquivo: "))
    menu = f"""----- MENU -----
    1- FATORIAL
    2- SEQUÊCIA DE FIBONACCI
    3- SEQUÊCIA SIMPLES
    4 - PRODUTO DA MULTIPLICAÇÃO
    5 - POTÊNCIA
    6 - SOMA ALEATÓRIA(
    7 - CONTAR VOGAIS E CONSOANTES \n"""
    print(menu)
    data = list(map(int,input("Digite a opção: ").split(" ")))
    
    
    while data[0] != 0:
        if data[0] == 1:
            entrada = int(input("Digite fatorial: "))
            result_Fatorial = fatorial(entrada)
            print(f"""> O fatorial é {result_Fatorial}""")
            gravar_Arquivo(name_File,[result_Fatorial])
        elif data[0] == 2:
            entrada = int(input("Digite o comprimento: "))
            result_Fibonacci = fibonacci(entrada)
            show_vector(result_Fibonacci)
            gravar_Arquivo(name_File, result_Fibonacci)
        elif data[0] == 3:
            entrada = list(map(int,input("Digite o inicio e fim da sequência(Ex:a b): ").split(" ")))
            result_Sequencia = sequecia_simples(entrada)
            show_vector(result_Sequencia)
            gravar_Arquivo(name_File,result_Sequencia)
        elif data[0] == 4:
            entrada = list(map(int,input("Digite a mulplicação(Ex: 2 4): ").split(" ")))
            result_Multiplicacao = produto_multiplicacao(entrada)
            print(result_Multiplicacao)
            gravar_Arquivo(name_File,[result_Multiplicacao])
        elif data[0] == 5:
            entrada = list(map(int,input("Digite a mulplicação(Ex: 2 4): ").split(" ")))
            result_Potenciacao = potencial(entrada)
            print(result_Potenciacao)
            gravar_Arquivo(name_File, [result_Potenciacao])
        elif data[0] == 6:
            entrada = int(input("Digite o tamanho do vetor: "))
            min_max = list(map(int,input("Digite o min e max(Ex: 2 4): ").split(" ")))
            result_Soma = soma_aleatoria(entrada,min_max)
            print(result_Soma)
            gravar_Arquivo(name_File, [result_Soma])
        elif data[0] == 7:
            entrada = str(input("Digite a frase: ")).split(" ")
            result_Vogais_consoante = contar_Vogais_consoantes(entrada)
            print(f"Vogais: {result_Vogais_consoante[0]} \n Consoantes: {result_Vogais_consoante[1]}")
            gravar_Arquivo(name_File, result_Vogais_consoante)
        data = list(map(int,input("Digite a opção: ").split(" ")))


main()