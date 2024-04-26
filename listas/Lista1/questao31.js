import { question } from "readline-sync"

//entrada(escreva numeros de 4 digitos em forma de base decimal)
var numero = Number(question('ESCREVA UM NUMERO DE 4 DIGITOS: '))

var unidadedem = Math.floor(numero/1000)
var passo1 = numero%1000
var centena = Math.floor(passo1/100)
var passo2 = passo1%100
var dezena = Math.floor(passo2/10)
var unidade = passo2 % 10
var decimal = unidade*2**0 + dezena*2**1 + centena*2**2 + unidadedem*2**3

console.log(`................................

O NUMERO EM BASE DECIMAL E ${decimal}

.......................................`)