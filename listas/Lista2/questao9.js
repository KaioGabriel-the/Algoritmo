import { question } from "readline-sync"

function verificacao(num){
    if(num/num === 1 && num/1===num || num/2===1 || num/3===1 || num/5===1 || num/7===1 || num/11===1){
        return 'é um numero primo'
    }else if(num/2 !== num && num/3 !== num && num/4 !==num && num/5 !==num && num/7 !== num && num/9 !== num && num/11!==num){
        return 'não é um numero primo'
    }else{
        return 'não é um numero primo'
    }
}

function print(text){
    return console.log(text)
}
 
function get_number(text){
    const numero = Number(question(text))
    return numero
}

function main(){
    //entrada
    const numero = get_number('ESCREVA O NUMERO: ')

    //processamento
    const primo = verificacao(numero)

    //saida
    print(`${primo}`)
}

main()