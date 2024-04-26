import { question } from "readline-sync"

const numero1 = Number(question('digite o primeiro numero: ')) 
const numero2 = Number(question('escreva o segundo numero: '))

const soma = numero1 + numero2
const diferenca = numero1 - numero2
const divisao = soma / diferenca

const mensagem = `-------------------
SOMA:${soma}
DIFERENCA:${diferenca}
SOMA/DIFERENCA:${divisao}
-----------------------------`

console.log(mensagem)

