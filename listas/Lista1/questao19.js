import { question } from "readline-sync"

const mensagem1 = `
.............DESCUBRA O VOLUME DA ESFERA..............
`
console.log(mensagem1)

const raio = Number(question('QUAL O VALOR DO RAIO DA CIRCUFERENCIA: '))

const pi = 3.14
const volume = 4*pi*raio**3/3

const mensagem = `........................

VALOR DO VOLUME DA ESFERA E:${volume.toFixed(2)}

'-'
............................`

console.log(mensagem)