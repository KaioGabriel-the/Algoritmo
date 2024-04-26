def main():

    nome = str(input('Nome da candidata: '))
    altura = int(input('Altura: '))
    peso = int(input('Peso: '))

    nome_ma =''
    altura_m =0
    nome_mp =''
    peso_m =0
    nome_na =''
    altura_n =0
    nome_np = ''
    peso_n = 0

    while nome != 'Fim':
        
      
      if altura > altura_m:
       altura_m= altura
       nome_ma = nome

      if altura < altura_n:
       altura_n = altura
       nome_na = nome

      if peso> peso_m:
       peso_m = peso
       nome_mp = nome

      if peso < peso_n: 
       peso_n = peso
       nome_np = nome

      nome = str(input('Nome da candidata: '))
      altura = int(input('Altura: '))
      peso = int(input('Peso: '))

    print(f'Mais alta - nome:{nome_ma} altura: {altura_m}')
    print(f'Menor - nome:{nome_na} altura: {altura_n}')
    print(f'Gorda - nome:{nome_mp} peso: {peso_m}')
    print(f'Mais alta - nome:{nome_np} peso: {peso_n}')

main()

