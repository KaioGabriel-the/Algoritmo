import { question, questionNewPassword } from "readline-sync"

//entrada(ecalcule a quantidade de dinheiro gasta por um fumante)

const anos = Number(question('QUANTOS ANOS ELE E FUMANTE: '))
const quantidade = Number(question('QUANTOS CIGARROS ELE FUMAR POR DIA: '))
const volor = Number(question('QUAL O VALOR DA CARTEIRA DE CIGARRO: '))

const passo = quantidade / 20 
const passo1 = anos*365 
const passo2 = passo * passo1
const passo3 = passo2 * volor 

console.log(`....................................

A QUANTIDADE DE CARTEIRAS DE CIGARROS QUE ELE FUMOU TODO ESSE TEMPO ${passo2}
A QUANTIDADE DE DINHEIRO GASTO ESSE TEMPO TODO ${passo3} reais

.................................................      `)