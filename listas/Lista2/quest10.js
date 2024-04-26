import { question } from "readline-sync"

function verificacao(a,aa,m,ma,d,da){
    if(a<=aa && m<=12 && d<=31){
        return "é uma data legivel"
    }else{
        return 'não é legivel'
    }
}

function get_number(text){
    const variavl = Number(question(text))
    return variavl
}

function main(){
    const ano = get_number('DIGITE O ANO: ')
    const mes = get_number('DIGITE O MES: ')
    const dia = get_number('DIGITE O DIA: ')
    const anoA = get_number('DIGITE O ANO ATUAL: ')
    const mesa = get_number('DIGITE O MES ATUAL: ')
    const diaa = get_number('DIGITE O DIA ATUAL: ')

    const data = verificacao(ano,anoA,mes,mesa,dia,diaa)

    console.log(`${data}`)
}

main()