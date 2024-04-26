//Faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
//a) "Telefonou para a vítima ?"
//b) "Esteve no local do crime ?"
//c) "Mora perto da vítima ?"
//d) "Devia para a vítima ?"
//e) "Já trabalhou com a vítima ?"
//O algoritmo deve no final emitir uma classificação sobre 
//a participação da pessoa no crime. Se a pessoa
//responder positivamente a 2 questões ela deve ser classificada como 
//"Suspeita", entre 3 e 4 como
//"Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado 
//como "Inocente".

import { question } from "readline-sync"

function pessoa(p1,p2,p3,p4,p5){
    if(p1 === 'sim' && p2 ==='sim' && p3 === 'sim' && p4 === 'sim' && p5 === 'sim'){
        return 'assasino'
    }else if(p1=== 'não' && p2 === 'não' && p3=== 'não' && p4 === 'não' && p5 === 'não'){
        return 'inocente'
    }else if(p1=== 'sim' && p2 === 'sim' && p3=== 'sim' && p4 === 'sim'){
        return 'cumplice'
    }else if(p2 === 'sim' && p3=== 'sim' && p4 === 'sim' && p5 === 'sim'){
        return 'cumplice'
    }else if(p1 === 'sim' && p3=== 'sim' && p4 === 'sim' && p5 === 'sim'){
        return 'cumplice'
    }else if(p1 === 'sim' && p3=== 'sim' && p2 === 'sim' && p5 === 'sim'){
        return 'cumplice'
    }else if(p1 === 'sim' && p2=== 'sim' && p4 === 'sim' && p5 === 'sim'){
        return 'cumplice'
    }else if(p2 === 'sim' && p1=== 'sim' && p4 === 'sim' && p3 === 'sim'){
        return 'cumplice'
    }else if(p1 === 'sim' && p2 ==='sim' && p3 === 'sim'){
        return 'cumplice'
    }else if(p1 === 'sim' && p2 ==='sim' && p4 === 'sim'){
        return 'cumplice'
    }else if(p1 === 'sim' && p2 ==='sim' && p5 === 'sim'){
        return 'cumplice'
    }else if(p3 === 'sim' && p2 ==='sim' && p5 === 'sim'){
        return 'cumplice'
    }else if(p4 === 'sim' && p2 ==='sim' && p5 === 'sim'){
        return 'cumplice'
    }else if(p1 === 'sim' && p3 ==='sim' && p4 === 'sim'){
        return 'cumplice'
    }else if(p4 === 'sim' && p3 ==='sim' && p5 === 'sim'){
        return 'cumplice'
    }else if(p1 === 'sim' && p5 ==='sim' && p4 === 'sim'){
        return 'cumplice'
    }else if(p1 === 'sim' && p3 ==='sim' && p5 === 'sim'){
        return 'cumplice'
    }else{
        return 'suspeita'
    }
}

function main(){
    const pergunta1 = String(question('Telefonou para a vítima ?'))
    const pergunta2 = String(question('Esteve no local do crime ?'))
    const pergunta3 = String(question('Mora perto da vítima ?'))
    const pergunta4 = String(question('Devia para a vítima ?'))
    const pergunta5 = String(question('Já trabalhou com a vítima ?'))

    const resultado = pessoa(pergunta1,pergunta2,pergunta3,pergunta4,pergunta5)

    console.log(`${resultado}`)
}

main()