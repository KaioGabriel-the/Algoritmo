import { question } from "readline-sync"

function media(num,num1,num2,num3,num4){
    const soma = num+num1+num2+num3+num4
    const divisao = soma / 5
    return divisao
}

function maior(pass01,num,num1,num3,num4){
    let numeros = ''
    
    if(num>pass01){
        numeros = `${num}`
    }if (num1>pass01){
        numeros = `${num1}`
    }if (num3>pass01){
        numeros = `${num3}`
    }if (num4>pass01){
        numeros = `${num4}`
    }
    return numeros
}

function get_number(text){
    return Number(question(text))
}

function main(){
    const numero = get_number('DIGITE UM NUMERO: ')
    const numero1 = get_number('DIGITE UM NUMERO: ')
    const numero2 = get_number('DIGITE UM NUMERO: ')
    const numero3 = get_number('DIGITE UM NUMERO: ')
    const numero4 = get_number('DIGITE UM NUMERO: ')

    const passo1 = media(numero,numero1,numero2,numero3,numero4)
    const passo2 = maior(passo1,numero,numero1,numero2,numero3,numero4)

    console.log(`
    media:${passo1}
    os numeros acima da media:${passo2}`)
}

main()