import { question } from "readline-sync"

function verificacao(lad1,lad2,lad3){
    if(lad2+lad3<lad1){
        return 'não é um triangulo'
    }else if(lad1+lad3<lad2){
        return 'não é um triangulo'
    }else if(lad2+lad1<lad3){
        return 'não é um triangulo'
    }else{
        return `é um triangulo ${classificacao(lado1,lado2,lado3)}`
    }

} 
    
function classificacao(lad1,lad2,lad3){
    if(lad1 === lad2 && lad1 === lad3 && lad2 === lad3){
        return 'equilatero'
    }else if(lad1 !== lad2 && lad1 !== lad3 && lad2 !== lad3){
        return 'escaleno'
    }else{
        return 'isosceles'
    }
}
function print(text){
    return console.log(text)
}
 
function get_number(text){
    const numero = Number(question(text))
    return numero
}
 
function main(){
    //entrada
    const lado1 = get_number('ESCREVA O PRIMEIRO LADO: ')
    const lado2 = get_number('ESCREVA O SEGUNDO LADO: ')
    const lado3 = get_number('ESCREVA O TERCEIRO LADO: ')

    //processamento
    const soma = verificacao(lado1,lado2,lado3)
    
    //saida 
    print(`........................
    
    ${soma}
    
    .................................`)
}

main()