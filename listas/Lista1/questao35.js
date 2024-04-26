import { question } from "readline-sync"

const mensagem = `.........................

DIGITE UM NUMERO DE 4 ALGARISMOS E DESCUBRA A SOMA ENTRE OS MEMBROS

............................................`
console.log(mensagem)

const numero = Number(question('DIGITE O NUMERO: '))

const unidadem = Math.floor(numero/1000)
const passo = numero % 1000
const centena = Math.floor(passo/100)
const passo1 = passo % 100
const dezena = Math.floor(passo1/10)
const unidade = passo1 % 10
const soma = unidadem + centena + dezena + unidade

const mensagem1 = `.....................................

A SOMA DE TODOS OS ALGARISMO DE ${numero} E ${soma}

.......................................`

console.log(mensagem1)