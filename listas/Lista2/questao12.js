import { question } from "readline-sync"

function get_number(text){
    return Number(question(text))
}

function i_p(num){
    if(num % 2 === 0){
        return 'O NUMERO É PAR'
    }else{
        return 'O NUMERO E IMPAR'
    }
}

function main(){
    const numero = get_number('DIGITE UM NUMERO: ')

    const verificacao = i_p(numero)

    console.log(`${verificacao}`)
}

main()