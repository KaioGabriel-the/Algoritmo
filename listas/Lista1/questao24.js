import { question } from "readline-sync"

const m = (question('QUANTOS METROS VOCE DESEJA TRANSFORMA EM CENTIMETROS: '))

const c = m*100

console.log(`A QUANTIDADE DE CENTIMETROS E:${c}`)