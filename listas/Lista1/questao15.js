import { question } from "readline-sync"

const mensagem1 = `CALCULE A AREA DE UM TRIANGULO COM APENAS O VALOR DA BASE E DA ALTURA`
console.log(mensagem1)
var base = Number(question('VALOR DA BASE: '))
var altura = Number(question('VALOR DA ALTURA: '))

var passo1 = base*altura
var passo2 = passo1/2

const mensagem = `.........................

A AREA DO TRIANGULO E ${passo2}

'-'

...................................`

console.log(mensagem)