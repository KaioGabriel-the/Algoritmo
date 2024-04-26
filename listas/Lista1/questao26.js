import { question } from "readline-sync"

//entrada(SEMANAS E DIAS)
var numerod = Number(question('DIGITE A QUANTIDADE DE DIAS: '))

var semanas = Math.floor(numerod/7)
var dias = numerod%7

console.log(`..........................
SEMANAS:${semanas}
DIAS:${dias}
.....................................`)