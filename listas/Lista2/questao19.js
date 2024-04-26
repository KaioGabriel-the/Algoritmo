import { question } from "readline-sync"

function imc(pes,alt){
    const resultado = pes / (alt**2)
    return resultado
}

function saude(formu){
    if(formu<25){
        return 'peso normal'
    }else if(formu===25 && formu<=30){
        return 'obeso'
    }else{
        return 'obesidade morbida'
    }
}

function get_number(text){
    return Number(question(text))
}

function main(){
    const altura = get_number('digite sua altura: ')
    const peso = get_number('digite seu peso: ')

    const formula = imc(peso,altura)
    const classificando = saude(formula)

    console.log(`${classificando}`)
}

main()