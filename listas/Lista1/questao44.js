import { question } from "readline-sync"

//entrada(descubra a quantidade de cobre e zinco para produzir latão)

const latao = Number(question('QUAL A QUANTIDADE DE LATÃO QUE VOCê DESEJA PRODUZIR: '))

const cobre = latao*0.7
const zinco = latao*0.3

console.log(`................................

QUANTIDADE NECESSARIA DE COBRE:${cobre}
QUANTIDADE NECESSARIA DE COBRE:${zinco}

..................................................`)

