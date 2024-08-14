def possui_letra(palavra,conj_letras):

    for letra in palavra:

        if letra in conj_letras:
            return True
    
    return False

def split_manual(string):

    list_proibida = []

    for chr in string:

        if chr == "," or chr == " ":
            True
        else:
            list_proibida.append(chr)

    return list_proibida

def main():

    menu =f'       -----MENU----- \n 0- ENCERRAR O PROGRAMA \n 1- PALAVRAS COM MAIOR OU IGUAL A \"N\" LETRAS \n 2- PALAVRAS COM MENOS OU IGUAL A \"N\" LETRAS \n 3- PALAVRAS COM QUANTIDADE DE \"N\" DE LETRAS \n 4- PALAVRAS QUE TENHAM A LETRA \"N\" \n 5- PALAVRAS QUE NÃO TENHAM A LETRA \"N\" 6- LETRAS PROIBIDAS \n'
    print(menu)
    estado = int(input("QUAL OPÇÃO:"))

    while estado > 0:
        fin = open('words.txt')

        if estado == 1:

            qtd_chr = int(input('QUAL A QUANTIDADE DE LETRAS: '))

            for line in fin:
                word = line.strip()
                    
                if len(word) >= qtd_chr:
                    print(word)
                    
            fin.close()
            
            print(menu)

            estado = int(input("QUAL OPÇÃO:"))

        elif estado == 2:

            qtd_chr = int(input('QUAL A QUANTIDADE DE LETRAS: '))

            for line in fin:
                word = line.strip()
                    
                if len(word) <= qtd_chr:
                    print(word)
                    
            fin.close()
            
            print(menu)

            estado = int(input("QUAL OPÇÃO:"))

        elif estado == 3:
            

            qtd_chr = int(input('QUAL A QUANTIDADE DE LETRAS: '))

            for line in fin:
                word = line.strip()
                    
                if len(word) == qtd_chr:
                    print(word)
                    
            fin.close()
            
            print(menu)

            estado = int(input("QUAL OPÇÃO:"))

        elif estado == 4:

            n = str(input('QUAL A LETRA: '))

            plv_n = []
            plv_s_n = []

            for line in fin:
                line = fin.readline()

                for letra in line:

                    if letra == str(n):
                        print(f'{line}')
                        plv_n.append(line)
                        break
                    else:
                        plv_s_n.append(line)
            
            fin.close()

            porcentagem = (len(plv_n)/len(plv_s_n)) * 100

            resultado = f'PORCENTAGEM DE PALAVRAS COM A LETRA {n}  \n {porcentagem:.2f}%'

            print(resultado)

            print(menu)

            estado = int(input("QUAL OPÇÃO:"))

        elif estado == 5:

            n = str(input('QUAL A LETRA: '))

            plv_n = []
            plv_s_n = []

            for line in fin:
                line = fin.readline()

                for letra in line:

                    if letra == str(n):
                        plv_n.append(line)
                    elif letra != str(n):
                        print(f'{line}')
                        plv_s_n.append(line)
            
            fin.close()

            porcentagem = (len(plv_s_n)/len(plv_n)) * 100

            resultado = f'PORCENTAGEM DE PALAVRAS QUE NÃO TENHAM A LETRA {n} \n {porcentagem:.2f}%'

            print(resultado)

            print(menu)

            estado = int(input("QUAL OPÇÃO:"))

        elif estado == 6:

            proibidas = str(input("QUAIS SÃO AS LETRAS PROIBIDAS(*SEPARE POR VIRGULA COM ESPAÇO EX: a, b): "))
            list_proibidas = split_manual(proibidas)

            qtd_pl = 0

            for line in fin:
                
                if not possui_letra(line,list_proibidas):
                    qtd_pl+= 1
                
            print(qtd_pl)

            fin.close()

            porcentagem = (len(plv_s_n)/len(plv_n)) * 100

            resultado = f'PORCENTAGEM DE PALAVRAS QUE NÃO TENHAM A LETRA {n} \n {porcentagem:.2f}%'

            print(resultado)

            print(menu)

            estado = int(input("QUAL OPÇÃO:"))


main()