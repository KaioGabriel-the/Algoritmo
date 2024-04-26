import { question } from "readline-sync"

function venceu(c_1,c_2,c_3){

    if(c_1>c_2 && c_1>c_3){
        return console.log('Canditado 1')
    }else if(c_2>c_1 && c_2>c_3){
        return console.log('Canditado 2')
    }else{
        return console.log('Canditado 3')
    } 

}

function main(){

    const flag = Number(question('Quantidade de votos: '))

    let giros = 0
    let c_1 = 0
    let c_2 = 0
    let c_3 = 0
    let nulos = 0
    let brancos = 0

    for(let i = 1 ; i <= flag ; i++ ){

        giros += 1

        console.log(`Candidato 1: 1
        Candidato 2: 2
        Candidato 3: 3
        Nulos: 9
        Brancos: 0`)
        
        let votos = Number(question('Voto: '))

        if(votos===1){
            c_1 += 1
        }else if(votos===2){
            c_2 += 1
        }else if(votos===2){
            c_3 += 1
        }else if(votos===9){
            nulos += 1
        }else if(votos===0){
            brancos += 1
        }
    }

    console.log(`......................
    Canditado 1:
    Canditado 2:
    Canditado 3
    Nulos:
    Brancos: 
    Vencedor:${venceu(c_1,c_2,c_3)}`)
}

main()