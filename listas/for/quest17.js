import { question } from "readline-sync";

function main(){

    const flag = Number(question('Digite o limite: '))
    let soma = 0

    for(let i = 1 ; i<=flag ; i++ ){

        soma += 1/i

        console.log(`1/${i} = ${soma.toFixed(2)}`)
    }

    console.log(`....................
    Soma final = ${soma.toFixed(2)}`)
}

main()