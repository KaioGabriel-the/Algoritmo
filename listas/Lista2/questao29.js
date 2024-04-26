//Um número é um quadrado perfeito quando a 
//raiz quadrada do número é igual à soma das dezenas
//formadas pelos seus dois primeiros e dois últimos dígitos.
//Exemplo: √9801 = 99 = 98 + 01. O número 9801 é um quadrado perfeito.
//Escreva um algoritmo que leia um número de 4 dígitos
//e verifique se ele é um quadrado perfeito.

import { question } from "readline-sync"

function verificacao(p0,p1){
    if(p0 == p1){
        return `a raiz quadrada é ${p0}
        e é um quadrado perfeito`
    }else if(p0 !== p1){
        return `a raiz quadrada é ${p0},
        mas não é um quadrado perfeito`
    }else{
        return 'erro'
    }
}

function separacao(num){
    const dp = Math.floor(num / 100)
    const du = num % 100
    const resultado = dp +du
    return resultado
}

function get_number(text){
    return Number(question(text))
}

function main(){
   const numero = get_number('digite um numero: ')

   const pass0 = Math.sqrt(numero)
   const pass1 = separacao(numero)
   const pass2 = verificacao(pass0,pass1)

   console.log(`${pass2}`)
}

main()