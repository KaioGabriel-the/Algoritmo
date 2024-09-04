def sao_iguais(entrada):
    if entrada[0] == entrada[1] and entrada[2] == entrada[3]:
        return True
    else:
        return False


def diagonal_principal(entrada):
    if entrada[2] - entrada[0] == entrada[3] - entrada[1]:
        return True
    else:
        return False


def diagonal_secundaria(entrada):
    if entrada[2] - entrada[0] == entrada[1] - entrada[3]:
        return True
    else:
        return False


def movimento(entrada):
    if sao_iguais(entrada):
        return 0
    elif diagonal_secundaria(entrada) or diagonal_principal(entrada):
        return 1
    else:
        return 2


def main():
    entrada = list(map(int,input().split(" ")))
    result = movimento(entrada)
    print(result)
    

main()