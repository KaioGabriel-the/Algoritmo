def contador_leds(caso):
    pass

def input_automatico(text,min,max):

    #Pedindo dados e entrada;
    dados = int(input(text))

    #Filtragem de min e max;
    if dados <= min  and dados >= max :
        return dados
    else:
        input_automatico(text,min,max)

def main():

    #numeros de vezes o problema vai girar
    numero_vezes = input_automatico("",1,10**3)

    for i in range(numero_vezes):
        caso = input_automatico("",1,10**100)
        qtd_leds = contador_leds(caso)
main()