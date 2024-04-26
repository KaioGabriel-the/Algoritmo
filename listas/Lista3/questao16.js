//O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
//Até 5 Kg Acima de 5 Kg
//File R$ 4,90 por Kg R$ 5,80 por Kg
//Alcatra R$ 5,90 por Kg R$ 6,80 por Kg
//Picanha R$ 6,90 por Kg R$ 7,80 por Kg
//Para atender a todos os clientes, cada cliente poderá levar apenas
//um dos tipos de carne da promoção,
//porém não há limites para a quantidade de carne por cliente.
//Se compra for feita no cartão Tabajara o
//cliente receberá ainda um desconto de 5% sobre o total a compra.
//Escreva um programa que peça o tipo
//e a quantidade de carne comprada pelo usuário e gere um cupom fiscal,
//contendo as informações da
//compra: tipo e quantidade de carne, preço total, tipo de pagamento,
//valor do desconto e valor a pagar.

import { question } from "readline-sync"

function c_d(car,cart){
    const desconto = car * 0.05

    if(cart === 'sim'){
        return `${desconto}`
    }else{
        return `${car}`
    }
}

function valor(tp,k){

    const file1 = k*4.9
    const file2= k*5.8
    const alacatra1 =k*5.9
    const alacatra2 =k*6.8
    const picanha1 =k*6.9
    const picanha2 =k*7.8
    
    if(tp === 'file' && k<=5){
        return`${file1}`
    }else if(tp === 'file' && k>5){
        return`${file2}`
    }else if(tp === 'alcatra' && k<=5){
        return`${alacatra1}`
    }else if(tp === 'alcatra' && k>5){
        return`${alacatra2}`
    }else if(tp === 'picacnha' && k<=5){
        return`${picanha1}`
    }else if(tp === 'picanha' && k>5){
        return`${picanha1}`
    }
}

function main(){
    const tipo = String(question('tipo de carne: '))
    const kg = Number(question('quantidade(kg): '))
    const cartão = String(question('você possui o cartao tabajara: '))

    const carne = valor(tipo,kg)
    const desconto = c_d(carne,cartão)

    console.log(`........................

    tipo e quantidade de carne:${tipo}
    preço total:${carne}
    tipo de pagamento:com cartao tabajara - 5%  outros meios não tem descontos
    valor do desconto:com cartao tabajara - 5% 
    valor a pagar:${desconto}

    ..............................................`)
}

main()