import { question } from "readline-sync"

function c_a(a,an){
    const diferenca = a - an
    return diferenca
}

function get_number(text){
    const numero = Number(question(text))
    return numero
}

function c_m(m,mn,d,dn){
   const diferenc = m - mn 
   const dias = dn - d
   const dias2 = dias / 30
   const soma = (diferenc + dias2) / 12
   return soma
}

function main(){
    const ano = get_number ('DIGITE O ANO ATUAL: ')
    const mes = get_number ('DIGITE O MES ATUAL: ')
    const dia = get_number ('DIGITE O DIA ATUAL: ')
    const anon = get_number('DIGITE O SEU ANO DE NASCIENTO: ')
    const mesn = get_number('DIGITE O MES DE SEU NASCIMENTO: ')
    const dian = get_number('DIGITE O DIA DE SEU NASCIMENTO: ')

    const anos = c_a(ano,anon)
    const meses_dias = c_m(mes,mesn,dia,dian)
    const total = (anos +(-1)*meses_dias.toFixed(2)) 

    console.log(`A SUA IDADE É ${total}`)
}

main()