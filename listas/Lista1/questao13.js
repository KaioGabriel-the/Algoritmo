import {question} from "readline-sync"

var reais = Number(question('ESCREVA O VALOR EM REAIS QUE QUISER: '))

var porcentagem = reais*0.7

const mensagem = `......................................
VALOR QUE VOCE ESCREVEU:${reais}
70% DO VALOR QUE VOCE ESCREVEU:${porcentagem}
....................................

'-'`

console.log(mensagem)