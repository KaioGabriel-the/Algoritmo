def main():

    passageiro = str(input('Digite o nome do passageiro: '))
    nome_sobrenome = passageiro.split(' ')

    print(f'{nome_sobrenome[(len(nome_sobrenome)-1)]}/{nome_sobrenome[0]}')

main()