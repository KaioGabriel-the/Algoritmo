def main():

  variavel = int(input('Escolha de qual numero deseja escrever a tabuada: '))
  variavel2 = int(input('Qual o limite da sua tabuada: '))

  limite = variavel2 + 1

  for numero in range(limite):
    print(f'------------\n{variavel} X {numero} = {variavel * numero} \n ------------')

main()