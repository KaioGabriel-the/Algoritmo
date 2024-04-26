import { question } from "readline-sync"

//entrada(escreva um numero de 3 digitos e faça a diferença entre o numero e o seu inverso)
const numero = Number(question('DIGITE UM NUMERO DE 3 ALGARISMO: '))

const centena = Math.floor(numero/100)
const passo1 = numero % 100
const dezena = Math.floor(passo1/10)
const unidade = passo1 % 10
const uniao = `${unidade}${dezena}${centena}`
const diferenca = numero - uniao

console.log(`............................

O SEU NUMERO:${numero}
O INVERSO:${uniao}
A DIFERENCA ENTRE O NUMERO:${diferenca}

...............................`)
