def main():

    soma_idade_mulheres = 0
    soma_idade_homens = 0
    qtd_mulheres = 0
    qtd_mulheres_solteiras = 0
    qtd_homens = 0
    qtd_homens_solteiros = 0 
    qtd_mulheres_divorciadas_31mais = 0

    print(f'------- MENU -------- 1 - Participante 2 - Mostrar Resumo 0 - Sair >>> ')

    opcao = int(input('Digite sua opção: '))

    while opcao != 0:

        if opcao == 1:
            
            sexo = int(input('Sexo(1-Masc. 2-Femin.): '))
            idade = int(input('Idade: '))
            opcoes_estado_civil = print(f'Estado Civil: 1- Casado 2- Solteiro 3- Divorciado 4- Víuvo:')
            estado_civil = int(input(f'{opcoes_estado_civil} Digite seu estado civil:'))

            if sexo == 1:
                qtd_homens += 1
                soma_idade_homens += idade
            if estado_civil == 2:
                qtd_homens_solteiros += 1
            
            else:
                qtd_mulheres += 1
                soma_idade_mulheres += idade
            if estado_civil == 2:
                qtd_mulheres_solteiras+=1
            elif estado_civil == 3 and idade > 30:
                qtd_mulheres_divorciadas_31mais+=1
        elif opcao == 2:

            media_idade_mulheres = soma_idade_mulheres / qtd_mulheres
            media_idade_homens = soma_idade_homens / qtd_homens
            perc_homens_solteiros = (qtd_homens_solteiros / qtd_homens) * 100
            perc_mulheres_solteiras = (qtd_mulheres_solteiras / qtd_mulheres) * 100

            resultado = print(f' · Média de idade das mulheres: {media_idade_mulheres:.2f}; · Média de idade dos homens: {media_idade_homens:.2f}; · O percentual de homens solteiros: {perc_homens_solteiros:.2f}%; · O percentual de mulheres solteiras: {perc_mulheres_solteiras:.2f}%; · A quantidade de mulheres divorciadas acima de 30 anos: {qtd_mulheres_divorciadas_31mais}.')
            print(resultado)

        opcao = int(input('Digite sua opção: '))

main()
