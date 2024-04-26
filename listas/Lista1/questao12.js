import { question } from "readline-sync"

var salario = Number(question('QUAL O VALOR DO SEU SALARIO: '))

var aumento = salario*0.25
var novo = salario+aumento

const mensagem = `.....................................

SALARIO SEM O AUMENTO:${salario} 
SALARIO COM O AUMENTO DE 25%:${novo}

...........................................`

console.log(mensagem)