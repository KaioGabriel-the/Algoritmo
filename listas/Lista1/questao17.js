import { question } from "readline-sync"

const mensagem1 = `
............DESCUBRA A AREA DO RETANGULO........`
console.log(mensagem1)

const variavel = Number(question('QUAL O VALOR DA BASE: '))
const variavel1 = Number(question('QUAL O VALOR DA ALTURA: '))

const area = variavel*variavel1

const mensagem = `..........................

A AREA DO RETANGULO E ${area}

'-'

..............................`

console.log(mensagem)