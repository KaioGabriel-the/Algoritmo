import { question } from "readline-sync"

function verificacao(at,an,ma,mn,da,dn){
    const i_ano = at - an
    const i_mes = ma - mn
    const i_dia = da - dn

    return `anos:${i_ano} mes:${i_mes} dia:${i_dia}`
}

function get_number(text){
    return Number(question(text))
}

function main(){
    const ano_nascimento = get_number('digite o ano de seu nascimento:')
    const mes_nascimento = get_number('digite o mes de seu nascimento:')
    const dia_nascimento = get_number('digite o ano de seu nascimento:')
    const ano_atual = get_number('digite o ano seu ano atual:')
    const mes_atual = get_number('digite o ano seu atual:')
    const dia_atual = get_number('digite o ano seu atual:')

    const idade = verificacao(ano_atual,ano_nascimento,mes_atual,mes_nascimento,dia_atual,dia_nascimento)
    
    console.log(`${idade}`)
}

main()