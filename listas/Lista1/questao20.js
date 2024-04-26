import { question } from "readline-sync"

const mensagem1 = `
............TRANSFORMCAO DE TEMPERATURA(ºC-->ºF)................
`
console.log(mensagem1)

const c = Number(question('QUAL A TEMPERATURA EM ºC: '))

const f = 9*c+160/5

const mensagem = `..........................

${c}ºc e o que vale a ${f}ºf

'-'
.................................`

console.log(mensagem)