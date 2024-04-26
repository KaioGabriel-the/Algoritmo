def main():

    entra1= str(input(''))
    entra2= str(input(''))
    entra3= str(input(''))

    if entra1 == 'vertebrado':
        if entra2 == 'ave':
            if entra3 == 'carnivoro':
                print(f'aguia')
            else:
                print(f'pomba')
        else:
            if entra3 == 'onivoro':
                print(f'homem')
            else:
                print(f'vaca')
    else:
        if entra2 == 'inseto':
            if entra3 =='hematofago':
                print(f'pulga')
            else:
                print(f'lagarta')
        else:
            if entra3 == 'hematofago':
                print(f'sanguessuga')
            else:
                print(f'minhoca')

main()
                