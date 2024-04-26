import { question } from "readline-sync"

//entrada(distribuição de notas de caixas eletronicos)
const valor = Number(question('VALOR QUE DESEJA SACAR: '))

const cinquenta = Math.floor(valor/50)
const passo1 = valor % 50
const dez = Math.floor(passo1/10)
const passo2 = passo1 % 10
const cinco = Math.floor(passo2/5)
const um = passo2 % 5 

console.log(`...............................

*QUANTIDADE DE NOTAS A SEREM DISTRIBUIDAS

50:${cinquenta}
10:${dez}
5:${cinco}
1:${um}

..........................................`)