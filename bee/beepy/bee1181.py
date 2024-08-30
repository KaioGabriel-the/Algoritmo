from functools import reduce


def create_vector(linhas,colunas):
    matriz = []
    for l in range(linhas):
        linha = []
        for c in range(colunas):
            elemento = input(str())
            linha.append(float(elemento))
        matriz.append(linha)
    
    return matriz


def main():
    linha = int(input())
    operacao = input()
    matriz = create_vector(12,12)


    sum = reduce(lambda x, y : x + y,matriz[linha])
    if operacao == "M":
        sum = round(sum/len(matriz[linha]),1)
    
    print(f"{sum:.1f}")


main()