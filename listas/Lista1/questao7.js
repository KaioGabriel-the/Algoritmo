import { question } from "readline-sync"

const questao = `Resolva a soma dos dois primeiros numeros e a diferenca entre os dois ultimos...
...........POR FAVOR COLOQUE OS NUMEROS AQUI EM BAIXO...........`
console.log(questao)

const numero1 = Number(question('Primeiro numero: '))
const numero2 = Number(question('Segundo numero: '))
const numero3 = Number(question('Terceiro numero: '))

const soma = numero1+numero2
const diferença = numero2-numero3

const mensagem = `------------------------------------
A soma entre o primeiro e segundo numero e igual a ${soma}
A diferenca entre o segundo e o terceiro numero e igual a ${diferença}
------------------------------------`

console.log(mensagem)