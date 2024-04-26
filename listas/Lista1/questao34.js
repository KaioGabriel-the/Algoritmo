import { question } from "readline-sync"

//entrada (leia 3 numeros e faça a media deles)

var numero1 = Number(question('ESCREVA O PRIMEIRO NUMERO: '))
var numero2 = Number(question('ESCREVA O SEGUNDO NUMERO: '))
var numero3 = Number(question('ESCREVA O TERCEIRO NUMERO: '))

var soma = numero1 + numero2 + numero3
var media = soma / 3.

console.log(`.............................................

A MEDIA ENTRES OS NUMEROS ${numero1},${numero2} E ${numero3}
E IGUAL A ${media.toFixed(2)}

.......................................................`)