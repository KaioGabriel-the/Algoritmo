import { question } from "readline-sync"

var ms = Number(question('quantos m-s voce que transforma em km-h; '))

var kmh = ms*3.6

console.log(`A quantidade em de km-h e ${kmh}`)