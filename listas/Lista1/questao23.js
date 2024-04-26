import {question} from 'readline-sync'

const mensagem1 = `
.............TRANSFORMANDO KG EN G...............
`
console.log(mensagem1)

var kg = Number(question('QUANTOS KG VOCE DESEJA TRANSFORMA EM G: '))

var g = kg*1000

const mensagem = `.............................

A QUANTIDADE EM G E ${g}

'-'

.........................................`
console.log(mensagem)