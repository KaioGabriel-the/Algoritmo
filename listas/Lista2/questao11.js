import { question } from "readline-sync"

function get_number(text){
    return Number(question(text))
}

function roleta(op,num1,num2,num3){
    if(op === 1){
        return `O NUMERO QUE SAIU FOI ${num3}`
    }else if(op === 2){
        return `O NUMERO QUE SAIU FOI ${num1}`
    }else if(op === 3){
        return `O NUMERO QUE SAIU FOI ${num2}`
    }else{
        return 'ERRO'
    }
}

function main(){
    const opcao = get_number('ESCOLHA ENTRE 1,2,3: ')
    const numero1 = get_number('DIGITE UM NUMERO:')
    const numero2 = get_number('DIGITE UM NUMERO:')
    const numero3 = get_number('DIGITE UM NUMERO:')

    const pass01 = roleta(opcao,numero1,numero2,numero3)

    console.log(`${pass01}`)

}

main()