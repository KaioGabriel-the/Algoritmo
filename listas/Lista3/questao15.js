//Uma fruteira está vendendo frutas com a seguinte tabela de preços:
//Até 5 Kg Acima de 5 Kg
//Morango R$ 2,50 por Kg R$ 2,20 por Kg
//Maçã R$ 1,80 por Kg R$ 1,50 por Kg
//Se o cliente comprar mais de 8 Kg em frutas ou o valor total
//da compra ultrapassar R$ 25,00, receberá
//ainda um desconto de 10% sobre este total.
//Escreva um algoritmo para ler a quantidade (em Kg) de
//morangos e a quantidade (em Kg) de maças adquiridas
//e escreva o valor a ser pago pelo cliente.

import { question } from "readline-sync"

function soma(mor,mac){
    const morang = mor *2.5
    const morang2 = mor *2.
    const maca= mac *1.8
    const maca2= mac *1.5
    const soma1= morang+maca
    const soma2= morang+maca2
    const soma3= morang2+maca
    const soma4= morang2+maca2
    const soma1_1= (morang+maca)*0.1
    const soma2_1= (morang+maca2)*0.1
    const soma3_1= (morang2+maca)*0.1
    const soma4_1= (morang2+maca2)*0.1
    if(mor<=5 && mac<=5 && `${somadasfrutas}`<8 && soma1<=25){
        return `${soma1}`
    }if(mor<=5 && mac<=5 &&`${somadasfrutas}`>8 && soma1<=25){
        return `${soma1_1}`
    }if(mor<=5 && mac<=5 `${somadasfrutas}`>8 && soma1>=25){
        return `${soma1_1}`
    }if(mor>=5 && mac<=5 `${somadasfrutas}`>8 && soma3>=25){
        return `${soma3_1}`
    }if(mor<=5 && mac>=5 `${somadasfrutas}`>8 && soma2>=25){
        return `${soma2_1}`
    }if(mor>=5 && mac>=5 `${somadasfrutas}`>8 && soma4>=25){
        return `${soma4_1}`
    }
}

function somadasfrutas(mo,ma){
    const somakg =mor + mac
    return somakg
}

function main(){
    const morangos = Number(question('morangos(KG): '))
    const macas = Number(question('maça(KG): '))

    const valor = soma(morangos,macas)

    console.log(`${valor}`)
}

main()