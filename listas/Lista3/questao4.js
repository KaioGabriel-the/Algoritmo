//Leia 2 (duas) notas parciais de um aluno, 
//calcule a média e escreva a mensagem:
//o "Aprovado", se a média alcançada for maior ou igual a sete;
//o "Reprovado", se a média for menor do que sete;
//o "Aprovado com Distinção", se a média for igual a dez.

import { question } from "readline-sync"

function media(num1,num2){
    const M = (num1 + num2)/2

    if(M>=7){
        return 'aprovado'
    }else if(M<7){
        return 'reprovado'
    }else if(M===10){
        return 'aprovado com distincao'
}
}

function get_number(text){
    const mensagem = (question(text))
    return mensagem
}

function main(){
    const numero1 = get_number('nota 1: ')
    const numero2 = get_number('nota 2: ')

    const situacao = media(numero1,numero2)

    console.log(`${situacao}`)

}

main()