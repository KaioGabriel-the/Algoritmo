import { question } from "readline-sync"

//entrada(leia a idade de uma pessoa em dias e escreva em anos,meses e dias)
const idade = Number(question('QUANTOS DIAS DE VIDA VOCE TEM: '))

const anos = Math.floor(idade/365)
const passo = idade % 360
const meses = Math.floor(passo/30)
const dias = passo % 30

console.log(`..........................................

A SUA IDADE EM ANOS E ${anos},MESES E ${meses} E DIAS E ${dias}

........................................................`)