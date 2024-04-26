import { question } from "readline-sync"

function verificacao(num){
    if(num>0){
        return 'é positivo'
    }else{
        return 'é negativo'
    }
}

function get_number(text){
    const mensagem = Number(question(text))
    return mensagem
}

function main(){
    const numero = get_number('digite um numero: ')

    const v = verificacao(numero)

    console.log(`${v}`)
}

main()
