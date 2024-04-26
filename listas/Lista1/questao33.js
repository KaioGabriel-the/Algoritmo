import { question } from "readline-sync"

//entrada(numero de 3 algarismo e a soma do numero com o inverso)
const numero = Number(question('DIGITE UM NUMERO: '))

const centena = Math.floor(numero/100)
const passo = numero % 100
const dezena = Math.floor(passo/10)
const unidade = passo % 10
const inverso = `${unidade}${dezena}${centena}`
const soma = numero + inverso

console.log(`...................................

NUMERO:${numero}
INVERSO:${inverso}
A SOMA DOS DOIS:${soma}

.........................................`)