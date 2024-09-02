from functools import reduce


def pegar_coluna(matriz,coluna):
   vetor_coluna = []

   for i in range(len(matriz)):
      elemento = matriz[i][coluna]
      vetor_coluna.append(elemento)
   
   return vetor_coluna


def create_matriz(linhas,colunas):
    matriz = []
    for l in range(linhas):
        linha = []
        for c in range(colunas):
            elemento = input(str())
            linha.append(float(elemento))
        matriz.append(linha)
    
    return matriz


def input_min_max(text):
  entrada = int(input(text))
  
  if 0 <= entrada <= 11:
     return entrada
  else:
     input_min_max(text)


def main():

   entrada = input_min_max("")
   operacao = str(input())
   matriz = create_matriz(12,12)
   coluna = pegar_coluna(matriz,entrada)
   soma = reduce(lambda x, y: x +y,coluna)
   if operacao == "S":
      print(soma)
   elif operacao == "M":
      print(round((soma/len(coluna)),1))


main()