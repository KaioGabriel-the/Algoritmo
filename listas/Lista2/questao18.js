import { question } from "readline-sync"

function soma(num,num1){
    const adicao = num+num1
    return adicao
}

function get_number(text){
    return Number(question(text))
}

function main(){
    const numero = get_number('escreva um numero: ')
    const numero1 = get_number('escreva um numero: ')

    const operacao = soma(numero,numero1)

    console.log(`O VALOR DA OPERACAO É ${operacao}`)
}

main()