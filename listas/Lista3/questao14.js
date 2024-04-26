//Um posto está vendendo combustíveis com a seguinte tabela de descontos:
//1. Álcool:
//· até 20 litros, desconto de 3% por litro
//· acima de 20 litros, desconto de 5% por litro
//2. Gasolina:
//· até 20 litros, desconto de 4% por litro
//· acima de 20 litros, desconto de 6% por litro.
//Escreva um algoritmo que leia o número de litros vendidos,
//o tipo de combustível (codificado da
//seguinte forma: A-álcool, G-gasolina), calcule e imprima
//o valor a ser pago pelo cliente sabendo-se que
//o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.

import { question } from "readline-sync"

function cacalculo(com,lit){
    const gasolinaate20 = (lit * 2.5)*0.04
    const gasolinaacima20 = (lit * 2.5)*0.06
    const alcoolate20 = (lit * 1.9)*0.03
    const alcoolacima20 = (lit * 1.9)*0.06

    if(com === 'g' && lit<=20){
        return `o valor a ser pago é ${gasolinaate20}`
    }else if(com === 'g' && lit>20){
        return `o valor a ser pago é ${gasolinaacima20}`
    }else if(com === 'a' && lit<=20){
        return `o valor ser pago é $${alcoolate20}`
    }else if(com === 'a' && lit>20){
        return `o valor ser pago é $${alcoolacima20}`
    }
}

function get_number(text){
    const mensagem = (question(text))
    return mensagem

}

function main(){
    const combustível = String(question('digite o tipo de combustivel: '))
    const litros = get_number('quantos litro: ')

    const valor = cacalculo(combustível,litros)

    console.log(`${valor}`)
}

main()