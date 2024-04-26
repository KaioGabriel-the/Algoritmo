import { question } from "readline-sync"

var kmh = Number(question('Quantos km-h voce deseja transforma em m-s: '))

const constante = 3.6
var ms = kmh/3.6

const mensagem = `${kmh} km-h corresponde a ${ms.toFixed(2)} m-s`

console.log(mensagem)