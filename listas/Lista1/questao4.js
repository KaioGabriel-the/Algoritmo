import { question } from "readline-sync"

var cotação = Number(question('cotacao atual do dolar: '))
var dolar = Number(question('quantidade de doloras que voce deseja transforma: '))

var reais = cotação*dolar

console.log(`O valor de ${dolar} dolares e ${reais.toFixed(2)} reais`)

