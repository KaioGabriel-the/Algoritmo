def main():

    menu =f'       -----MENU----- \n 0- ENCERRAR O PROGRAMA \n 1- PALAVRAS COM MAIOR OU IGUAL A \"N\" LETRAS \n 2- PALAVRAS COM MENOS OU IGUAL A \"N\" LETRAS \n 3- PALAVRAS COM QUANTIDADE DE \"N\" DE LETRAS \n'
    print(menu)
    estado = int(input("QUAL OPÇÃO:"))

    while estado > 0:
        fin = open('words.txt')

        if estado == 1:

            qtd_chr = int(input('Qual a quantidade de caracteres:'))

            for line in fin:
                word = line.strip()
                    
                if len(word) >= qtd_chr:
                    print(word)
                    
            fin.close()
            
            print(menu)

            estado = int(input("QUAL OPÇÃO:"))

        elif estado == 2:

            qtd_chr = int(input('Qual a quantidade de caracteres:'))

            for line in fin:
                word = line.strip()
                    
                if len(word) <= qtd_chr:
                    print(word)
                    
            fin.close()
            
            print(menu)

            estado = int(input("QUAL OPÇÃO:"))

        elif estado == 3:
            

            qtd_chr = int(input('Qual a quantidade de caracteres:'))

            for line in fin:
                word = line.strip()
                    
                if len(word) == qtd_chr:
                    print(word)
                    
            fin.close()
            
            print(menu)

            estado = int(input("QUAL OPÇÃO:"))

main()