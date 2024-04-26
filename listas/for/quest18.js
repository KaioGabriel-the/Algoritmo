import { question } from "readline-sync";

function main(){

    const flag = Number(question('Digite o limite: '))
    let soma = 0
    let decrecendo = flag
    for(let i = 1 ; i<=flag ; i++ ){

        if (decrecendo === 0){
            break
        }

        soma += i/decrecendo

        console.log(`${i}/${decrecendo} = ${soma.toFixed(2)}`)
        
        decrecendo -= 1
    }

    console.log(`....................
    Soma final = ${soma.toFixed(2)}`)
}

main()