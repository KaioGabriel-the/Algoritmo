import { question } from "readline-sync"

function main(){
    //entrada
    const numero1 = get_number('DIGITE O PRIMEIRO NUMERO: ')     
    const numero2 = get_number('DIGITE O SEU SEGUNDO NUMERO: ')

    //processamento
    const verificacao  =  igualdade(numero1,numero2)
    
    //saida
    console.log(`${verificacao}`)
}

function igualdade(num1,num2){
    if(num1 > num2){
        return 'O PRIMEIRO NUMERO É MAIOR QUE O SEGUNDO NUMERO'
    }else if(num2 > num1){
        return 'O SEGUNDO NUMERO É MAIOR QUE O PRIMEIRO NUMERO'
    }else{
        return 'TODOS OS NUMEROS SÃO IGUAIS'
    }
}

function get_number(text){
    const numero = Number(question(text))
    return numero
}


main()