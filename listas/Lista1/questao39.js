import { question } from "readline-sync"

//entrada(escreva 3 algarismo)
const numero1 = Number(question('ESCREVA O PRIMEIRO NUMERO: '))
const numero2 = Number(question('ESCREVA O SEGUNDO NUMERO: '))
const numero3 = Number(question('ESCREVA O TERCEIRO NUMERO: '))

const passo1 = (numero1 + numero2)**2
const passo2 = (numero2 + numero3)**2
const passo3 = passo1 + passo2 
const passo4 = passo3/2

console.log(`.......................

O RESULTADO E ${passo4}

..................................`)