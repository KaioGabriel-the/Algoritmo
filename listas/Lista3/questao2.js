//Leia uma letra, verifique se letra é "F" ou "M" e 
//escreva F - Feminino, M - Masculino, Sexo Inválido.

import { question } from "readline-sync"

function verificacao(l){

    if(l === 'f'){
        return 'femenino'
    }else if(l==='m'){
       return 'masculino'
    }else{
        return ' sexo indefinido'
    }
}

function main(){
    const letra = String(question('digite a letra: '))
    
    const validacao = verificacao(letra)

    console.log(`${validacao}`)
}

main()