import { question } from "readline-sync"

//entrada(calcule um sistema de equações)
const questao = `
ESSSE E O TIPO DE EQUAÇãO QUE PODE SER RESOLVIDA: ax + by = c
                                                  dx + ey = f
...............................................................`
console.log(questao)

const a = Number(question('ESCREVA O VALOR DE A: '))
const b = Number(question('ESCREVA O VALOR DE B: '))
const c = Number(question('ESCREVA O VALOR DE C: '))
const d = Number(question('ESCREVA O VALOR DE D: '))
const e = Number(question('ESCREVA O VALOR DE E: '))
const f = Number(question('ESCREVA O VALOR DE F: '))

const x = c*e - b*f / a*e - b*d
const y = a*f - c*d / a*e - b*d

console.log(`..............................

O VALOR DE X E ${x}
O VALOR DE Y E ${y}

......................................`)