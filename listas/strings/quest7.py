def main():

    verb = str(input('Digite o verbo: '))

    for i in range(0,1):

        palavra = ''

        for i in range(len(verb)-2):
            palavra += str(verb[i])
            i += 1

        print(f'''Verbos terminados em ER no presente
            
            {palavra + 'o'}
            {palavra + 'es'}   
            {palavra + 'e'}
            {palavra + 'emos'}
            {palavra + 'eis'}
            {palavra + 'em'}
                     ''')

main()
