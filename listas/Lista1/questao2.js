import {question} from 'readline-sync'

var horas = Number(question('Quantas horas voce que transforma em minutos; '))

var minutos = horas*60

console.log(`A quantidade de minutos é ${minutos}`)