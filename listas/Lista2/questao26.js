//Leia os 3 (três) lados 
//de um triângulo e identifique sua hipotenusa e seus catetos.

import { question } from "readline-sync"

function pt(l1,l2,l3){
    let numero = ''

    if (l1 > l2 && l1 > l3) {
        return `H=${l1}
                C=${l2}
                C=${l3}`
    }if(l2>l1 && l2>l3){
        return `H=${l2}
                C=${l1}
                C=${l3}`
    }if (l3 > l2 && l3 > l1) {
        return `H=${l3}
                C=${l2}
                C=${l3}`

    }else{
        return `erro`
    }
}

function get_number(text){
    return Number(question(text))
}

function main(){
    const lado1 = get_number('lado 1: ')
    const lado2 = get_number('lado 2: ')
    const lado3 = get_number('lado 3: ')
    
    const resultado = pt(lado1,lado2,lado3)

    console.log(`${resultado}`)
}

main()