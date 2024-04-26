//Leia as duas notas parciais obtidas por um aluno numa disciplina
//ao longo de um semestre, e calcule a
//sua média. A atribuição de conceitos obedece à tabela abaixo:
//Média de Aproveitamento Conceito
//Entre 9.0 e 10.0 A
//Entre 7.5 e 9.0 B
//Entre 6.0 e 7.5 C
//Entre 4.0 e 6.0 D
//Entre 4.0 e zero E
//O algoritmo deve mostrar na tela as notas, a média,
//o conceito correspondente e a mensagem
//“APROVADO” se o conceito for A, B ou C ou
//“REPROVADO” se o conceito for D ou E.

import { question } from "readline-sync"

function media(num,num1){
    const div = (num + num1)/2
    if (di>=9 || div === 10){
        return `....................................
        
        Média de Aproveitamento Conceito
        Entre 9.0 e 10.0 A
        Entre 7.5 e 9.0 B
        Entre 6.0 e 7.5 C
        Entre 4.0 e 6.0 D
        Entre 4.0 e zero E
        
        Conceit:A
        Media:${div}
        Situacao:aprovado
        
        .................................`
    }else if(di>=7.5 || div === 8.9){
        return `....................................
        
        Média de Aproveitamento Conceito
        Entre 9.0 e 10.0 A
        Entre 7.5 e 9.0 B
        Entre 6.0 e 7.5 C
        Entre 4.0 e 6.0 D
        Entre 4.0 e zero E
        
        Conceit:B
        Media:${div}
        Situacao:aprovado
        
        .................................`
    }else if(di>=6 || div === 7.4){
        return `....................................
        
        Média de Aproveitamento Conceito
        Entre 9.0 e 10.0 A
        Entre 7.5 e 9.0 B
        Entre 6.0 e 7.5 C
        Entre 4.0 e 6.0 D
        Entre 4.0 e zero E
        
        Conceit:C
        Media:${div}
        Situacao:aprovado
        
        .................................`
    }else if(di>=4 || div === 5.9){
        return `....................................
        
        Média de Aproveitamento Conceito
        Entre 9.0 e 10.0 A
        Entre 7.5 e 9.0 B
        Entre 6.0 e 7.5 C
        Entre 4.0 e 6.0 D
        Entre 4.0 e zero E
        
        Conceit:D
        Media:${div}
        Situacao:reprovado
        
        .................................`
    }else if(di>=0 || div === 3.9){
        return `....................................
        
        Média de Aproveitamento Conceito
        Entre 9.0 e 10.0 A
        Entre 7.5 e 9.0 B
        Entre 6.0 e 7.5 C
        Entre 4.0 e 6.0 D
        Entre 4.0 e zero E
        
        Conceit:E
        Media:${div}
        Situacao:reprovado
        
        .................................`
    }else {
        return 'erro'
    }
}

function get_number(text){
    const mensagem = (question(text))
    return mensagem
}

function main(){
    const numero = get_number('nota 1: ')
    const numero1 = get_number('nota 2: ')

    const validacao = media(numero,numero1)
}

main()