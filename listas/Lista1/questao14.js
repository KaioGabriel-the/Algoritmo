import { question } from "readline-sync"

const nota1 = Number(question('NOTA 1: '))
const peso1 = Number(question('PESO 1: '))
const nota2 = Number(question('NOTA 2: '))
const peso2 = Number(question('PESO 2: '))
const nota3 = Number(question('NOTA 3: '))
const peso3 = Number(question('PESO 3: '))

const passo1 = nota1*peso1+nota2*peso2+nota3*peso3
const passo2 = peso1+peso2+peso3
const passo3 = passo1/passo2

const mensagem = `........................................

A MEDIA PONDERADA DAS SUAS NOTAS E:${passo3}

.............................................

'-'
`

console.log(mensagem)