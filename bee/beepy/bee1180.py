def achar_menor(vetor):
  menor = vetor[0]
  index = 0
  for i in range (len(vetor)):
    if vetor[i] < menor:
      menor = vetor[i]
      index = i
  return [menor,index]
def create_vector(entrada):
  elemento = (str(input())).split(" ")
  vector = []
  for i in range(entrada):
    new = int(elemento[i])
    vector.append(new)
  return vector 

def input_min_max(text):
  entrada = int(input(text))
  if 1 <= entrada <= 1000:
    return entrada
  else:
    input_min_max(text)

def main():
  entrada = input_min_max(" ")
  vetor = create_vector(entrada )
  menor = achar_menor(vetor)
  print(f"Menor valor: {menor[0]}")
  print(f"Posicao: {menor[1]}")
  
main()
