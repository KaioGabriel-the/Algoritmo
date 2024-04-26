import{question} from 'readline-sync'

var numero = (question('ESCREVA UM NUMERO DE TRES DIGITOS: '))

var primeiro = Math.floor(numero/100)
var resto = numero % 100
var segundo = Math.floor(resto/10)
var terceiro = resto % 10

const mensagem = `O NUMERO QUE VOCE ESCREVEU FOI ESTE ${numero}
O SEU INVERSO E ESTE ${terceiro}${segundo}${primeiro}`

console.log(mensagem)