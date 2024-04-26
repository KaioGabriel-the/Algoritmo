import {question} from 'readline-sync'

const variavel1 = Number(question('digite um numero:'))
const variavel2 = Number(question('digite outro numero:'))

const um = variavel1
const dois = variavel2

const mensagem = `numero normal:${variavel1}${variavel2}
numero invertido:${variavel2}${variavel1}`

console.log(mensagem)





