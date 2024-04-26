import { question } from "readline-sync"

function get_number(text){
    return Number(question(text))
}

function quadro(num,num2){
    const q = num**2
    const q2 = num2**2
    return `o resultado é ${q} e ${q2}`
}

function div(num,num1){
    const divisao = (num + num1)/num1
    return divisao
}

function mul_so(num,num2){
    const soma_mult = (num + num2)*num
    return soma_mult
}

function soma(num,num2){
    const pass = num + num2 + 1
    return pass
}

function i_p(num,num2){
    if(num % 2 === 0 && num2 % 2 === 0){
        return 'O NUMERO É PAR'
    }else if(num % 2 === 0 && num2 % 2 != 0){
        return `O primeiro numero é par e o segundo numero é impar`
    }else if(num % 2 != 0 && num2 % 2 === 0){
        return `O primeiro numero é impar e o segundo numero é par`
    }else{
        return 'O NUMERO E IMPAR'
    }
}
function operacoes(num,num2,p1){
    if(p1 === 1){
        return `o resultado é este ${soma(num,num2)}`
    }else if(p1 === 2){
        return`o resultado é este ${i_p(num,num2)}`
    }else if(p1 === 3){
        return `o resultado é este ${mul_so(num,num2)}`
    }else if(p1 === 4){
        return `o resultado é este ${div(num,num2)}`
    }else {
        return `o resultado é este ${quadro(num,num2)}`
    }
}

function divisao(num1,num2){
    const resultado = num1 % num2
    return resultado
}

function main(){
    const numero = get_number('digite um numero: ')
    const numero2 = get_number('digite um numero: ')

    const passo1 = divisao(numero,numero2)
    const passo2 = operacoes(numero,numero2,passo1)

    console.log(`${passo2}`)
}

main()