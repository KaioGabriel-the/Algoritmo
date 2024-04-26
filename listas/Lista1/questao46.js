import { question } from "readline-sync"

//entrada(valor da entrada e das prestações da mercadoria)
const valor = Number(question('QUAL O VALOR DA MERCADORIA: '))

const entradat1p = valor*0.35
const parcelast1s = valor*0.65/2
const entradat2p = valor/3

console.log(`..............................

*SE O VALOR DO PRODUTO FOR PAR(COM EXCEÇÃO DOS DIVISIVES POR 3)

ENTRADA:${entradat1p.toFixed(2)}
PARCELAS:${parcelast1s.toFixed(2)}

*SE O NUMERO FOR IMPAR(COM EXCEÇÃO DOS TERMINDOS EM 11)

ENTRADA:${entradat2p}
PARCELAS:${entradat2p}

...............................................`)