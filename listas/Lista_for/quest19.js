import { question } from "readline-sync";

function main(){

    const flag = Number(question('Digite o limite: '))
    let soma = 0
    let sucessor = 0
    let anterior = 0
    let a_dividendo = 1
    let a_divisor = flag
    let s_divisor = 2
    let s_dividendo = flag - 1
    
    for(let i = 1 ; i<=flag ; i++ ){


        anterior = a_dividendo / a_divisor   
        sucessor =s_dividendo / s_divisor
        let subtracao = anterior - sucessor
        soma += subtracao
        a_dividendo += 2
        s_dividendo += 2
        a_divisor = a_divisor - 2
        s_dividendo = a_dividendo - 2 
    }

    console.log(`....................
    Soma final = ${soma.toFixed(2)}`)
}

main()