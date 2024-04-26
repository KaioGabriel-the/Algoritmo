import { question } from "readline-sync"

const numeroh = (question('QUANTAS HORAS VOCE QUE TRANSFORMA: '))

const semanas = Math.floor(numeroh/168)
const passo = numeroh%168
const dias = Math.floor(passo/24)
const horas = passo%24 

console.log(`................................

SEMANAS:${semanas}
DIAS:${dias}
HORAS:${horas}

.........................................`)