def main():
    razao = int(input('Digite a razao: '))
    primeiro_termo = int(input('Digite o primeiro termo: '))
    ultimo = int(input('Digite o ultimo termo: '))

    termos_novo = primeiro_termo
    termos = 0

    while termos != ultimo:
        termos_novo = termos_novo * razao
        termos = termos_novo
        print(f'{termos}')
    
    print(f'{termos}')

main()
