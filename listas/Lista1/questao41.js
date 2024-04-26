import { question } from "readline-sync"

//entrada(calcule o custo de um corro ao consumidor)
const fabrica = Number(question('DIGITE O CUSTO DE FABRICA: '))

const impostos = fabrica*0.45
const distribuidor = fabrica*0.28
const soma = fabrica + impostos + distribuidor

console.log(`...............................

CUSTO DE FABRICA:${fabrica}
IMPOSTOS:${impostos}
DISTRIBUIDOR:${distribuidor.toFixed(2)}
CUSTO TOTAL PARA O CONSUMIDOR:${soma}

....................................................`)