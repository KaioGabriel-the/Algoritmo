//Para o cálculo de uma folha de pagamento, sabendo que os descontos 
//são do Imposto de Renda, que
//depende do salário bruto (conforme tabela abaixo) e 
//3% para o Sindicato e que o FGTS corresponde a
//11% do salário bruto, mas não é descontado (é a empresa que deposita).
//O salário líquido corresponde
//ao salário bruto menos os descontos.
//O programa deverá pedir ao usuário o valor da sua hora e a
//quantidade de horas trabalhadas no mês.
//Desconto do IR:
//o Salário Bruto até R$ 900,00 (inclusive) - isento
//o Salário Bruto até R$ 1.500,00 (inclusive) - desconto de 5%
//o Salário Bruto até R$ 2.500,00 (inclusive) - desconto de 10%
//o Salário Bruto acima de R$ 2.500,00 - desconto de 20%
//Escreva na tela as informações, dispostas conforme o exemplo abaixo.
//No exemplo o valor da hora é 5 e
//a quantidade de hora é 220.
//Salário Bruto: (5 * 220) : R$ 1100,00
//(-) IR (5%) : R$ 55,00
//(-) INSS ( 10%) : R$ 110,00
//FGTS (11%) : R$ 121,00
//Total de descontos : R$ 165,00
//Salário Liquido : R$ 935,00

import { question } from "readline-sync"

function ir(sal){
    const s900 = sal
    const s1500 = sal*0.05
    const s2500 = sal*0.1
    const s2500mais =sal*0.20

    if(sal<=900){
        return `${s900}`
    }else if(sal>900 && sal <=1500){
        return `${s1500}`
    }else if(sal>1500 && sal <=2500){
        return `${s2500}`
    }else if(sal>2500){
        return`${s2500mais}`
    }
}

function sindicato(sal){
    const desconto = sal * 0.03
    return desconto
}

function FGTS(sal){
    desconto = sal * 0.11
    return desconto
}

function main(){
    const salario = Number(question('digite seu salario'))

    const p1 = FGTS(salario)
    const p2 = sindicato(salario)
    const p3 = ir(salario)
    const p4 = p2+p3-salario
    const p5 = p2 + p3

    console.log(`
    
    Salário Bruto: R$ ${salario}
//(-) IR (5%-20%) : R$${p3}
//(-) Sindicato( 3%) : R$${p2}
//FGTS (11%) : R$ ${p1}
//Total de descontos : R$ ${p5}
//Salário Liquido : R$ ${p3}
`)
}

main()