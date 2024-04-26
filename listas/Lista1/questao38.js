import { question } from "readline-sync"

//entrada(escreva duas fracoes,some e escreva o resultado em forma de fracao)
const fracao1n = Number(question('ESCREVA O NUMERADOR DA PRIMEIRA FRACAO: '))
const fracao1d = Number(question('ESCREVA O DENOMINADOR DA PRIMEIRA FRACAO: '))
const fracao2n = Number(question('ESCREVA O NUMERADOR DA SEGUNDA FRACAO: '))
const fracao2d = Number(question('ESCREVA O DENOMINADOR DA SEGUNDA FRACAO: '))

const numerador1 = fracao1n * fracao2d + fracao2n * fracao1d
const denominador1 = fracao1d * fracao2d

console.log(`.................................................

A SOMA DAS FRACOES E ${numerador1}/${denominador1}

*NAO E UMA FRACAO IRREDUTIVEL 

...................................................`)