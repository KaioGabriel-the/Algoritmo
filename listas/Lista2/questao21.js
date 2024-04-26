import { question } from "readline-sync"

function get_number(text){
    return Number(question(text))
}

function aproximacao (n_f){
    const difereca = n_f - Math.trunc(n_f)
    return difereca
}

function arrendonda(f,n){
    const superior = Math.trunc(n) + 1
    const inferior = Math.trunc(n) - 1
    if (f > 0.05){
   return `${superior}`
   } else if( f < 0.05 ){
   return `${inferior}`
   }else {
    return 'erro'
   }
}
function main(){
    const numero_fracionario = get_number('digete um numero decimal de ate duas casas: ')

    const formula = aproximacao(numero_fracionario)
    const formula2 = arrendonda(formula,numero_fracionario)

    console.log(`o numero arrendondado e ${formula2}`)
}

main()