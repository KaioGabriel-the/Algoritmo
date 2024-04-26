//Leia a hora do início de um jogo e a hora de fim do jogo 
//(cada hora é composta por 2 variáveis inteiras:
//hora e minuto). Calcule e escreva a duração do jogo (horas e minutos), 
//sabendo-se que o tempo
//máximo de duração do jogo é de 24 horas e que ele pode iniciar-se
// em um dia e terminar no dia
//seguinte.

import { question } from "readline-sync"

function verificacao(hj,min){
    if(hj <=23 && min<=59){
        return `a hora é ${hj} e os minuntos são ${min}`
    }else{
        return 'o jogo acabou'
    }
}

function minuntos(mi,mf){
    const minunt= mf-mi
    return minunt
}

function hora(hi,hf){
    const hora = hf - hi
    return hora
}

function get_number(text){
    return Number(question(text))
}

function main(){
    const horas_inicio = get_number('digite a hora do inicio do jogo: ')
    const minutos_inicio = get_number('digite a minutos do incio do jogo: ')
    const horas_final = get_number('digite a hora do fim do jogo: ')
    const minutos_final = get_number('digite os minutos do fim do jogo: ')

    const hora__do_jogo = hora(horas_inicio,horas_final)
    const minutos = minuntos(minutos_inicio,minutos_final)
    const v = verificacao(hora__do_jogo,minutos)

    console.log(`${verificacao}`)
}

main()