import { question } from "readline-sync"

function atemil(salario){
    if (salario <= 1000){
        return 1
    }else{
        return 0
    }
}

function main(){

    const flag = Number(question('População: '))

    let giros = 0
    let s_salario = 0
    let qtd_filhos = 0
    let qtd_ate1000 = 0

    for(let i = 1 ; i <= flag ; i++ ){

        giros += 1

        let salario = Number(question('Qual a quantidade do seu salario: '))

        qtd_ate1000 += atemil(salario)

        s_salario += salario

        let filhos = Number(question('Qual a quantidade de filhos: '))

        qtd_filhos += filhos

    }

    console.log(`......................
    Media dos salarios:${(s_salario/giros).toFixed(2)}
    Media dos filhos:${(qtd_filhos/giros).toFixed(2)}
    Percentual de pessoas que recebem ate 1000: ${(qtd_ate1000/giros).toFixed(2)}`)
}

main()