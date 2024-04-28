def main():

  frase = str(input('Digite uma frase: ')).lower()

  frase_final = ''

  for i in range(0,len(frase)):
    variavel = str(frase[i])
    variavel1= str(frase[i])
    frase_final += str(variavel + variavel1)

  print(f'''.................
  {frase_final}''')
            
main()