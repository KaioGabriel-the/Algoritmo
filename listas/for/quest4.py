def main():

   a0 = int(input('Digite a A0 da PA: '))
   razao = int(input('Digite a razao da PA: '))
   flag = int(input('Limite: '))

   for elemento in range(1,flag + 1):
      print(f'A{elemento}:{a0*razao**(elemento-1)}')

main()