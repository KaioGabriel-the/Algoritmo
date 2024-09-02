def create_vector(tamanho):
    matriz = []
    for l in range(tamanho):
        linha = []
        for c in range(tamanho):
            elemento = 1
            linha.append(int(elemento))
        matriz.append(linha)

    return matriz


def main():
    tamanho = int(input())
    while tamanho != 0:
        vector = create_vector(tamanho)
        matriz = []

        for l in range(len(vector)):
            linha = ""
            for e in range(len(vector)):
                linha += f" {vector[l][e]}"
            matriz.append(linha)

        for i in matriz:
            print(i)
        
        print("")
        tamanho = int(input())


main()
