import { question } from "readline-sync"

function get_numero(text){
   const numero = Number(question(text))
   return numero
}

function igualdade(num,num1,num3){
  if(num === num && num1 === num3 && num === num3){
    return 'TODOS OS NUMEROS SÃO IGUAIS'
  }else{
    return 'NEM UM DOS NUMEROS SÃO IGUAIS'
  }
  
}

function main(){
  //entrada
  const numero = get_numero('DIGITE O PRIMEIRO NUMERO: ')
  const numero1 = get_numero('DIGITE O SEGUNDO NUMERO: ')
  const numero3 = get_numero('DIGITE O TERCEIRO NUMERO:')
  
  //PROCESSAMENTO

  const verificacao = igualdade(numero,numero1,numero3)
  //saida
  console.log(` A RESPOSTA CERTA É ${verificacao}`)
}

main()