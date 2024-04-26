import { question } from "readline-sync"

//entrada(calcule a distancia entre dois pontos no plano cartesiano)

const ponto1X = Number(question('ESCREVA O X DO PRIMEIRO PONTO: '))
const ponto1Y = Number(question('ESCREVA O Y DO PRIMEIRO PONTO: '))
const ponto2X = Number(question('ESCREVA O X DO SEGUNDO PONTO: '))
const ponto2Y = Number(question('ESCREVA O Y DO SEGUNDO PONTO: '))

const x = (ponto2X - ponto1X)**2
const y = (ponto2Y - ponto1Y)**2
const diferenca = x - y 
const raiz = Math.sqrt(diferenca)

console.log(`..........................................

A DISTANCIA MEDIA ENTRES ESSES DOIS PONTOS E ${raiz.toFixed(2)}

..........................................`)