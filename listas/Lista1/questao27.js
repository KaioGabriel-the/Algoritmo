import { question } from "readline-sync"

var numeros = Number(question('QUAL A QUANTIDADE DE SEGUNDOS: '))

var horas = Math.floor(numeros/3600)
var passo = numeros % 3600
var minutos = Math.floor(passo/60)
var segundos = passo % 60 

console.log(`......................
HORAS:${horas}
MINUTOS:${minutos}
SEGUNDOS:${segundos}
..........................`)