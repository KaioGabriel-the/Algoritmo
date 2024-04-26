import { question } from "readline-sync"

//entrada(transforme meses em anos e mese)
const numerom = Number(question('QUANTOS MESES: '))

const anos = Math.floor(numerom/12)
const meses = numerom%12 

console.log(`..................................

*ANOS:${anos}
*MESES:${meses}

.......................................`)