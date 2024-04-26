//Existem números de 4 dígitos (entre 1000 e 9999) que obedecem à seguinte 
//característica: se dividirmos
//o número em dois números de dois dígitos,
//um composto pela dezena e pela unidade, e outro pelo
//milhar e pela centena, se somarmos estes dois
// novos números gerando um terceiro, o quadrado deste
//terceiro número é exatamente o número original de quatro dígitos. Por exemplo:
//2025 -> dividindo: 20 e 25 -> somando temos 45 -> 452 = 2025.

import { question } from "readline-sync"

function separacao(num){
    const dp = Math.floor(num / 100)
    const du = num % 100
    const soma = dp +du
    const resultado = soma**2
    return resultado
}

function get_number(text){
    return Number(question(text))
}

function main(){
    const numero = get_number('digite um numero:')

    const pass0 = separacao(numero)

    console.log(`${pass0}`)
}

main()