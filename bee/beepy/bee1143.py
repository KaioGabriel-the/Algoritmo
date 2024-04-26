def get_number_in_range(mensagem, min, max):
  numero = int(input(mensagem))

  if (numero < min or numero > max):
        print('Número inválido! Digite novamente')
        return get_number_in_range(mensagem, min, max)
    
  return numero

def quadrado_cubo(l,num):
    if l == 'q':
        return (num**2)
    elif l == 'c':
        return (num**3)
    
def main():

    numero = get_number_in_range('',1,1000)

    for i in range (1,numero+1):

        quadrado = quadrado_cubo('q',i)
        cubo = quadrado_cubo('c',i)

        print(f'''{i} {quadrado} {cubo}''')

main()
