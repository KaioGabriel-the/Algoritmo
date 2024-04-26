import {question} from 'readline-sync'

var numero1 = Number(question('PRIMEIRO NUMERO: '))
var numero2 = Number(question('SEGUND0 NUMERO: '))

var divisao = Math.floor(numero1 / numero2)
var resto = numero1 % numero2

console.log(`Divisao:${divisao} ;Resto:${resto}`)