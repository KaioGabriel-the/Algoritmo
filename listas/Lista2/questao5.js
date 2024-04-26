import { question } from "readline-sync"

function ordenacao(num1,num2,num3){
    if(num1>num2>num3){
        return `a sequencia é ${num1},${num2},${num3}`
    }else if(num2>num3>num1){
        return `a sequencia é ${num2},${num3},${num1}`
    }else if(num3>num2>num1){
        return `a sequencia é ${num3},${num2},${num1}`
    }else if(num1>num3>num2){
        return `a sequencia é ${num1},${num3},${num2}`
    }else if(num2>num1>num3){
        return `a sequencia é ${num2},${num1},${num3}`
    }else if (num3>num1>num2){
        return `a sequencia é ${num3},${num1},${num2}`
    }else{
        return `'_'`
    }
}

function print(text){
    return console.log(text)
}

function get_number(text){
    const numero = Number(question(text))
    return numero
}
function Main(){
    //entrada

    const numero1 = get_number('ESCREVA O PRIMEIRO NUMERO:')
    const numero2 = get_number('ESCREVA O SEGUNDO NUMERO: ')
    const numero3 = get_number('ESCREVA O TERCEIRO NUMERO: ')

    //processsamento
    const p1 = ordenacao(numero1,numero2,numero3)

    //saida
    print(`${p1}`)
    
} 

Main()