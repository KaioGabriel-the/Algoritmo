import { question } from "readline-sync"

function verificacao(pro1,pro2){
    if(pro1>pro2){
        return 'o professor 1 ganhar mais que o professor 2'
    }else if (pro2>pro1){
        return 'o professor 2 ganhar mais que o professor 1'
    }else{
        return 'os dois ganham igual'
    }
}

function calculo(proh1,prov1){
    const salario = proh1 * prov1
    return salario
}

function calculo2(proh2,prov2){
    const salario = proh2 * prov2
    return salario
}

function get_number(text){
    return Number(question(text))
}

function main(){
    const prof1h = get_number('p1-quantas horas voce trabalhar: ')
    const prof1v = get_number('p1-quanto vale 1 hora de aula: ')
    const prof2h = get_number('p2-quantas horas voce trabalhar: ')
    const prof2v = get_number('p2-quanto vale 1 hora de aula: ')

    const prof1 = calculo(prof1h,prof1v)
    const prof2 = calculo2(prof2h,prof2v)
    const mvp = verificacao(prof1,prof2)

    console.log(`
    salario do professor 1:${prof1}
    salario do professor 2:${prof2}
    
    ${mvp}`)
}

main()