import { question } from "readline-sync";

function main(){

    const flag = Number(question('Digite o limite: '))
    let soma = 0
    let atualizado = 0
    let anterior = 0
    let divisor = 1
    let rodas = 0
    

    for(let i = 1 ; i<=flag ; i++ ){

        if (rodas < 2){

            let atual = 1/divisor
            atualizado = anterior
            anterior = atual
            rodas += 1
        }
        else{
            let subtracao = atualizado - anterior
            soma += subtracao
            atualizado = 0
            anterior = 0 
            rodas = 0
        }
    }

    console.log(`....................
    Soma final = ${soma.toFixed(2)}`)
}

main()