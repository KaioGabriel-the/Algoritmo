from functools import reduce


def inferior(matriz,):
    elementos = []
    for l in range(len(matriz)):
        for c in range(len(matriz[l])):
            if (l == c or (l+c) == (len(matriz)-1)) and l == len(matriz) // 2:
                elemento = matriz[l][c]
                elementos.append(elemento)
    
    return elementos


def operation(opction, sum):
    if opction == "S":
        return sum
    elif opction == "M":
        return round(sum/12*12)


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
    opction = input(str(""))
    matriz = create_vector(12, 12)
    inferiores = inferior(matriz)
    sum = reduce(lambda x, y: x + y, inferiores)
    result = operation(opction, sum)
    print(result)


main()