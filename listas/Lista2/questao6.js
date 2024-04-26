import { question } from "readline-sync"

function classificando(ang1,ang2,ang3){
   if(ang1 === 0 || ang2 === 0 || ang3 === 0){
      return 'não existe triangulo com angulo 0'
   }else if(ang1 === 90 || ang2 === 90 || ang3 === 90){
      return 'é um triangulo retangulo'
   }else if(ang1<90 && ang2<90 && ang3<90){
      return 'é um triangulo acutângo'
   }else{
      return 'é um triangulo obtusângulo'
   }
}

function print(text){
   return console.log(text)
}

function get_number(text){
   const numero = Number(question(text))
   return numero
}

function Main(){
   // entrada 
   const angulo1 = get_number('DIGITE O PRIMEIRO ANGULO: ') 
   const angulo2 = get_number('DIGITE O SEGUNDO ANGULO: ')
   const angulo3 = get_number('DIGITE O TERCEIRO ANGULO: ')

   //processamento
   const triangulos = classificando(angulo1,angulo2,angulo3)

   //saida
   print(`${triangulos}`)
}

Main()