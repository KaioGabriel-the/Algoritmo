//Leia os coeficientes (A, B e C) de uma equações de 2° grau e escreva suas raízes. Vale lembrar que o
//coeficiente A deve ser diferente de 0 (zero).

import { question } from "readline-sync"

function raizes(A,B,C){
    if(A===0){
        return 'NÃO EXISTE A=0'
    }else{
        return `${resultado(A,B,C)}`

        function resultado(A,B,C){
            const delta = (B)**2 - 4*A*C
            const r2 = Math.sqrt(delta)
            const x1 = -B + r2 / 2*A
            const x2 = -B - r2 / 2*A
            
            return `x1=${x1} e x2=${x2}`
        }
    }
}

function get_number(text){
    return Number(question(text))
}

function main(){
    const a = get_number('digite a:')
    const b = get_number('digite b:')
    const c = get_number('digite c:')

    const formula = raizes(a,b,c)

    console.log(`${formula}`)
}

main()