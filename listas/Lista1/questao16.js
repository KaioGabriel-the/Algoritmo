import { question } from "readline-sync"


var variavel = Number(question('coloque o valor do lado do quadrado: '))

var quadrado = Math.pow(variavel,2)

const mensagem = `..............................

A AREA DO QUADRADO E ${quadrado}

'-'

.........................`

console.log(mensagem)