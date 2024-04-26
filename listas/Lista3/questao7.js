//As Organizações Tabajara resolveram dar um aumento de salário
//aos seus colaboradores e lhe
//contrataram para desenvolver o programa que
//calculará os reajustes. Escreva um algoritmo que leia o
//salário de um colaborador e o reajuste segundo o seguinte critério, 
//baseado no salário atual:
//o salários até R$ 280,00 (incluindo) : aumento de 20%
//o salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
//o salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
//o salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado,
//informe na tela:
//· o salário antes do reajuste;
//· o percentual de aumento aplicado;
//· o valor do aumento;
//· o novo salário, após o aumento.

import { question } from "readline-sync"

function valor(num){
    const rea1 = num*0.2
    const rea2 = num*0.15
    const rea3 = num*0.1
    const rea4 = num*0.05
    const sal1 = (num*0.2) + num
    const sal2 = (num*0.15) + num 
    const sal3 = (num*0.1) + num
    const sal4 = (num*0.05) + num

    if(num<=279.99){
        return `..........................

          o salário antes do reajuste:${num}
          o percentual de aumento aplicado:20%
          o valor do aumento:${rea1}
          o novo salário:${sal1}
          
          ...................................`
    }else if(num>= 280 || num<=699.99){
        return `..........................

          o salário antes do reajuste:${num}
          o percentual de aumento aplicado:20%
          o valor do aumento:${rea2}
          o novo salário:${sal2}
          
          ...................................`
    }else if(num>=700 || num <= 1499.99){
        return `..........................

    o salário antes do reajuste:${num}
    o percentual de aumento aplicado:20%
    o valor do aumento:${rea3}
    o novo salário:${sal3}
    
    ...................................`
    }else if(num>=1500){
        return `..........................

          o salário antes do reajuste:${num}
          o percentual de aumento aplicado:20%
          o valor do aumento:${rea4}
          o novo salário:${sal4}
          
          ...................................`
    }
}

function get_number(text){
    const mensagem = (question(text))
    return mensagem
}

function main(){
    const numero = get_number('digite seu salario: ')

    const salario = valor(numero)

    console.log(`${salario}`)

}

main()