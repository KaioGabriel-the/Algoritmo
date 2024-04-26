import { question } from "readline-sync"

function quadrante(ang){
    if(ang<=90){
        return 'esta dentro do primeiro quadrante'
    }else if(ang>90 && ang<=180){
        return 'esta dentro do segundo quadrante'
    }else if(ang>180 &&ang<=270){
        return 'esta dentro do terceiro quadrante'
    }else{
        return 'esta dentro do quarto quadrante'
    }
}

function get_number(text){
    return Number(question(text))
}

function main(){
    const angulo = get_number('escreva um angulo: ')

    const verificacao = quadrante(angulo)

    console.log(`${verificacao}`)
}

main()