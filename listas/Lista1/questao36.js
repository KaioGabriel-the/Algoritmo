import { question } from "readline-sync"

//entrada(peça a idade de uma pessoa em anos,meses e dias e escreva apennas em dias)
const idade = Number(question('QUANTOS ANOS VOCE TEM: '))
const idade1 = Number(question('QUANTOS MESES VOCE TEM: '))
const idade2 = Number(question('QUANTOS DIAS VOCE TEM: '))

const anos = idade * 12 
const passo = anos + idade1
const meses = passo * 30 
const dias = meses + idade2

console.log(`.....................................

A SUA IDADE APROXIMADAMENTE EM DIAS E ${dias}

..............................`)