import { question } from "readline-sync"

const mensagem1 = `
.........DESCUBRA O COMPRIMENTO DA CIRCUFERENCIA.........
`
console.log(mensagem1)

const raio = Number(question('QUAL O VALOR DO RAIO: '))

const pi = 3.14
const comprimento = 2*pi*raio

const mensagem = `.............................

O VALOR DO COMPRIMENTO DA CIRCUFERENCIA E:${comprimento}

'-'

...............................`

console.log(mensagem)