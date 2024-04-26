import { question } from "readline-sync"

function get_number(text){
    return Number(question(text))
}

function decomposicao(num,num1,num2){
    if(num > num1 && num > num2){
        return `o maior numero é ${num}`
    }else if(num1 > num && num1 > num2){
        return `o maior numero é ${num1}`
    }else if(num2 > num && num2 > num1){
        return`o maior numero é ${num2}`
    }else{
        return 'não é possiviel verifica esses numeros'
    }
}

function Main(){
  //entrada
  const numero = get_number('DIGITE O PRIMEIRO NUMERO: ')
  const numero1 = get_number('DIGITE O SEGUNDO NUMERO: ')
  const numero2 = get_number('DIGITE O TERCEIRO NUMERO: ')

  //processamento
  const verificacao = decomposicao(numero,numero1,numero2)

  //saida
  console.log(`${verificacao}`)
}

Main()