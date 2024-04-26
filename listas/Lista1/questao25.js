import { question } from "readline-sync"

//entrada(quantidade de km e m)

var metros = Number(question('QUANTOS METROS VOCE DESEJA TRANSFORMA: '))

var km = Math.floor(metros/1000)
var m = metros%1000

const mensagem = `...............................

KM:${km}
M:${m}

........................................`

console.log(mensagem)
