import {question} from 'readline-sync'

const mensagem1 = `
............TRANSFORMACAO DE TEMPERATURA(ºF--->ºC).................
`
console.log(mensagem1)

const f = Number(question('QUAL A TEMPERATURA EM ºF: '))

const c = 5*f-160/9

const mensagem = `............................

${f}ºf e o que vale ${c.toFixed(2)}ºc

'-'
............................`

console.log(mensagem)