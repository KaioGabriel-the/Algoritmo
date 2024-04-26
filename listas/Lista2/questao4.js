import { question } from "readline-sync"

function comparacao(dez,uni){
    if(dez === uni){
        return print('OS DOIS SÃO IGUAIS')
    }else{
        return print('OS DOIS SÃO DIFERENTES')
    }
}

function decomposicao(num){
    const dezena = Math.floor(num/10)
    const unidade = num % 10
    return dezena
}

function decomposicao1(num){
    const unidade = num % 10
    return unidade
}

function print(text){
    return console.log(text)
}

function get_number(text){
    const numero = Number(question(text))
    return numero
}

function Main(){
    //entrada
    const numero = get_number('DIGITE UM NUMERO DE 2 ALGARISMO: ')

    //processamento
    const p1 = decomposicao(numero)
    const p2 = decomposicao1(numero)
    const p3 = comparacao(p1,p2)

    //saida
    print(`${p3}`)
}

Main()