def verificacao_senha(senha):
    novamente = str(input('Digite a sua senha novamente: '))

    if senha != novamente:
        return verificacao_senha(senha)
    else:
        print(f'Senha verificada com sucesso!!!')

def main():

    senha = str(input('Digite sua senha: '))

    senha_novamente = verificacao_senha(senha)

main()