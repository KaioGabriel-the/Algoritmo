//Verifique a validade de uma senha fornecida pelo usuário.
// A senha é 1234. O algoritmo deve escrever
//uma mensagem de permissão de acesso ou não.

import { question } from "readline-sync"

function verificacao(sh){
    if(sh === 1234){
        return 'acesso concedido'
    }else{
        return 'acesso negado'
    }
}

function get_number(text){
    return Number(question(text))
}

function main(){
    const senha = get_number('digite a senha:')

    const vs = verificacao(senha)

    console.log(`${vs}`)
}

main()