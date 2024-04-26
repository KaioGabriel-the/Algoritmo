import { question } from "readline-sync"

const mensagem1 = `
..................TRANSFORMANDO KM EM M.....................
`
console.log(mensagem1)

var km = Number(question('QUANTOS KM VOCE DESEJA TRANSFORMA EM M: '))

var m = km*1000

const mensagem = `...........................

A QUANTIDADE DE M E:${m}

'-'

..............................................`

console.log(mensagem)