//Leia um número e escreva se o número é inteiro ou decimal.

import { question } from "readline-sync"

function verificacao(num){
    if(num>='0' ||  num <= '0'){
        return 'é um numero inteiro'
    }else if(num >= '0.0000' || num <= '0.0000'){
        return 'é um numero dcimal'
    }else{
        return 'erro'
    }
}

function main(){

    const numero = Number(question('digite um numero: '))

    const validacao = verificacao(numero)

    console.log(``)
}

main()