import { question } from "readline-sync"

//entranda(transforme minutos em dias,horas e minutos)
const numerom = Number(question(`QUANTOS MINUTOS: `))

const dias = Math.floor(numerom/1440)
const passo = numerom%1440
const horas = Math.floor(passo/60)
const minutos = passo%60 

console.log(`......................................

DIAS:${dias}
HORAS:${horas}
MINUTOS:${minutos}

......................................`)