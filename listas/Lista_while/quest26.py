def main():

    idade = int(input('Digite sua idade: '))
    opiniao = int(input('Digite sua opinião (1=ótimo, 2=bom, 3=regular, 4=péssimo): '))

    soma_pessoas = 0
    soma_idade = 0
    otimo = 0 
    bom = 0
    regular = 0
    pessimo = 0

    while idade != -1:

        if opiniao == 1:
            otimo += 1
        elif opiniao == 2:
            bom += 1
        elif opiniao == 3:
            regular += 1
        elif opiniao == 4:
            pessimo += 1

        soma_idade += 1
        soma_pessoas += 1

        idade = int(input('Digite sua idade: '))
        opiniao = int(input('Digite sua opinião (1=ótimo, 2=bom, 3=regular, 4=péssimo): '))

    media_idades = soma_idade / soma_pessoas
    percentua = bom/(bom+otimo+regular+pessimo)*100

    print(f'Media das idades:{media_idades}  Regular:{regular} Bom:{percentua}')

main()
  