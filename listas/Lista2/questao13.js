import { question } from "readline-sync"

function classs(num,num1,num2,num3,num4){
    if (num>num1>num2>num3>num4){
        return `o maior numero é ${num} o menor é ${num4}`
    }else if (num<num1<num2<num3<num4){
        return `o maior numero é ${num4} o menor é ${num}`
    }else if (num1>num2>num3>num4>num){
        return `o maior numero é ${num1} o menor é ${num}`
    }else if (num2>num3>num4>num>num1){
        return `o maior numero é ${num2} o menor é ${num1}`
    }else if(num3>num4>num>num1>num2){
        return `o maior numero é ${num3} o menor é ${num2}`
    }else if (num4>num>num1>num2>num3){
        return `o maior numero é ${num4} o menor é ${num3}`
    }else if(num>num2>num3>num4>num1){
        return `o maior numero é ${num} o menor é ${num1}`
    }else if (num>num3>num4>num1>num2){
        return `o maior numero é ${num} o menor é ${num2}`
    }else if(num>num4>num1>num2>num3){
        return `o maior numero é ${num} o menor é ${num3}`
    }else if (num1>num3>num4>num>num2){
        return `o maior numero é ${num1} o menor é ${num2}`
    }else if(num1>num4>num>num2>num3){
        return `o maior numero é ${num1} o menor é ${num3}`
    }else if (num1>num>num2>num3>num4){
        return `o maior numero é ${num1} o menor é ${num4}`
    }else if(num1>num>num3>num4>num2){
        return `o maior numero é ${num1} e o menor é ${num2}`
    }else if(num1>num>num4>num2>num3){
        return `o maior numero é ${num1} o menor é ${num3}`
    }else if (num2>num>num1>num4>num3){
        return `o maior numero é ${num2} o menor é ${num3}`
    }else if (num2>num1>num4>num3>num){
        return `o maior numero é ${num2} o menor é ${num}`
    }else if (num2>num1>num3>num>num4){
        return `o maior numero é ${num2} o menor é ${num3}`
    }else if(num3>num>num1>num2>num4){
        return `o maior numero é ${num3} o menor é ${num4}`
    }else if(num3>num4>num2>num1>num){
        return `o maior numero é ${num3} o menor é ${num}`
    }else if(num3>num4>num2>num>num1){
        return `o maior numero é ${num3} o menor é ${num2}`
    }else if (num4>num1>num2>num3>num){
        return `o maior numero é ${num4} o menor é ${num}`
    }else if (num4>num2>num3>num>num1){
        return `o maior numero é ${num4} o menor é ${num1}`
    }else if (num4>num3>num>num1>num2){
        return `o maior numero é ${num4} o menor é ${num2}`
    }else {
        return 'o sistema não é capaz de encontra a resposta'
    }
}

function get_number(text){
    return Number(question(text))
}

function main(){
    const numero = get_number('DIGITE UM NUMERO: ')
    const numero1 = get_number('DIGITE UM NUMERO: ')
    const numero2 = get_number('DIGITE UM NUMERO: ')
    const numero3 = get_number('DIGITE UM NUMERO: ')
    const numero4 = get_number('DIGITE UM NUMERO: ')

    const classificando = classs(numero,numero1,numero2,numero3,numero4)

    console.log(`${classificando}`)

}

main()