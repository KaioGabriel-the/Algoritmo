def classificacao_score1(soma1):
    if soma1 <= 1000:
        print(f'Muito bom')
    elif soma1 < 800:
        print(f'Bom')
    elif soma1 < 600:
        print(f'Regular')
    elif soma1 < 400:
        print(f'Baixo')

def classificacao_score2(soma):
    if soma <= 1000:
        print(f'Muito bom')
    elif soma < 701:
        print(f'Bom')
    elif soma < 501:
        print(f'Regular')
    elif soma < 301:
        print(f'Baixo')

def get_number_in_range(mensagem, min, max):
  numero = int(input(mensagem))

  if (numero < min or numero > max):
        print('Número inválido! Digite novamente')
        return get_number_in_range(mensagem, min, max)
    

  return numero


def main():

    criterio1 = get_number_in_range('Criterio 1: ',0,100)
    criterio2 = get_number_in_range('Criterio 2: ',0,100)
    criterio3 = get_number_in_range('Criterio 3: ',0,100)
    
    valor_criterio1 = criterio1 * 2.3
    valor_criterio2 = criterio2 * 0.3
    valor_criterio3 = criterio3 * 1.1
    
    soma1 = criterio1*10 + criterio2*10 + criterio3*10
    soma = valor_criterio1 + valor_criterio2 + valor_criterio3

    score1 = classificacao_score1(soma1)
    score2 = classificacao_score2(soma)

    print(f'Score 1.0: {soma1} - {score1} \n Score 2.0: {soma} - {score2}')

main()
