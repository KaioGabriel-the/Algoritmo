import { question } from "readline-sync"

//ESCREVA UM NUMERO INTEIRO SE TRES DIGITOS E SOME OS TRES DIGITOS

var numero = Number(question('digite um numero inteiro de tres algarismo: '))

var centena = Math.floor(numero/100)
var resto = numero % 100 
var dezena = Math.floor(resto/10)
var unidade = resto % 10
var soma = centena+dezena+unidade

const mensagem = `............................
A  soma de ${centena} + ${dezena} + ${unidade}
E  igual a ${soma}

obrigado por utiliza nosso sistema!!!`

console.log(mensagem)