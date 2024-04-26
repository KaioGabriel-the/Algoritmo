//Leia o preço de três produtos 
//e informe qual produto deve ser comprado,
//sabendo que a decisão é
//sempre pelo mais barato.

import { question } from "readline-sync"

function verificacao(p1,p2,p3){
    if(p1<p2 && p1<p3){
        return 'o produto primeiro é o mais barato'
    }else if(p2<p3 && p2>p1){
        return 'o segundo produto é o mais barato'
    }else if(p3>p1 && p3>p2){
        return 'o terceiro é o produto mais barato'
    }else{
        return 'erro'
    }
}

function get_number(text){
    const mensagem = (question(text))
    return mensagem
}

function main(){
    const produto = get_number('produto 1: ')
    const produto2 = get_number('produto 2: ')
    const produto3 = get_number('produto 3: ')

    const produto_barato = verificacao(produto,produto2,produto3)

    console.log(`${produto_barato}`)

}


main()