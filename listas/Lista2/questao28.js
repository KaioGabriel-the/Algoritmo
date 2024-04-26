//Leia as coordenadas cartesianas (x e y) de 2 (dois) pontos no plano,
//que corresponderão a dois cantos de
//um retângulo. Baseado nisto, calcule e escreva a área deste retângulo. 
//Lembre-se de que o valor da área
//não pode ser negativo.

import { question } from "readline-sync"

function area(x,y){
    const mult = x*y
    const elev = (mult)**2
    const resultado = Math.sqrt(elev)
    return resultado
}

function get_number(text){
    return Number(question(text))
}

function main(){
    const coordenada1 = get_number('digite x:')
    const coordenada2 = get_number('digite y:')

    const x_y = area(coordenada1,coordenada2)

    console.log(`a area é ${x_y}`)
    
}

main()