import { question } from "readline-sync"

function verificando(a1,a2,m1,m2,d1,d2){
    if(a1>a2){
        return 'a primeira data e maior'
    }else if(a2>a1){
        return 'a segunda e maior'
    }else if( a1 === a2 && m1 > m2){
        return 'o primeriro e maior'
    }else if( a1 === a2 && m2 > m1){
        return 'a sengunda e maior'
    }else if( a1 === a2 && m1 === m2 && d1>d2){
        return 'o primeriro e maior'
    }else if( a1 === a2 && m1 === m2 && d1<d2){
        return 'a segunda e maior'
    }else if(1 === a2 && m1 === m2 && d1===d2){
        return 'as datas sao iguais'
    }else{
        return 'erro'
    }
}

function get_number(text){
    return Number(question(text))
}

function main(){
   
    const ano1 =get_number('1 - digite o ano: ')
    const mes1 =get_number('1 - digite o mes: ')
    const dia1 =get_number('1 - digite o dia: ')
    const ano2 =get_number('2 - digite o ano: ')
    const mes2 =get_number('2 - digite o mes: ')
    const dia2 =get_number('2 - digite o dia: ')

    const verificacao = verificando(ano1,ano2,mes1,mes2,dia1,dia2)

    console.log(`${verificacao}`)
}
main()