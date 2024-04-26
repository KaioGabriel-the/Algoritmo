import { question } from "readline-sync"

var minutos = Number(question('quantos minutos voce deseja transforma em em horas: '))

var horas = minutos/60

console.log(`${minutos} corresponde a ${horas.toFixed(2)}`)