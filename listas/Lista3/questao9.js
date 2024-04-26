//Leia um número e exiba o dia correspondente da semana.
//(1-Domingo, 2- Segunda etc.), se digitar outro
//valor deve aparecer valor inválido.

import { question } from "readline-sync"

function semana(num){

    if(num === '1'){
        return 'segunda-feira'
    }else if(num === '2'){
        return 'terca-feira'
    }else if(num === '3'){
        return 'quarta-feira'
    }else if(num === '4'){
        return 'quinta-fira'
    }if(num === '5'){
        return 'sexta-feira'
    }if(num === '6'){
        return 'sabado'
    }else if(num === '7'){
        return 'domingo'
    }else{
        return 'erro'
    }

}

function get_number(text){
    const mensagem = (question(text))
    return mensagem
}

function main(){

    const numero = get_number('digite um numero: ')

    const dia = semana(numero)

    console.log(`${dia}`)
}

main()