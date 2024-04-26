//Leia um número inteiro menor que 1000 e imprima a quantidade de centenas,
//dezenas e unidades do
//número. Observando os termos no plural a colocação do "e",
//da vírgula entre outros. Exemplos:
//o 326 = 3 centenas, 2 dezenas e 6 unidades
//o 12 = 1 dezena e 2 unidades

import { question } from "readline-sync"

function decomposicao(num){
    const centena = Math.floor(num/100)
    const resto = num % 100
    const dezena = Math.floor(resto/10)
    const unidade = resto%10

    let conjuntos = ''

    if(centena > 0){
        return `centena:${centena}`
    }if(dezena > 0 ){
        return `dezena:${dezena}`
    }if(unidade > 0){
        return `unidade:${unidade}`
    }

    return conjuntos
}

function get_number(text){
    const mensagem = (question(text))
    return mensagem

}

function main(){
    const numero = get_number('digite um numero(tre algarismo): ')

    const verificacao = decomposicao(numero)

    console.log(`${verificacao}`)

}

main()