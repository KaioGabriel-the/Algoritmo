import { question } from "readline-sync"

function main(){

    const flag = Number(question('Pulação de bois: '))

    let giros = 0
    let magro = 0
    let id_magro = ''
    let gordo = 0
    let id_gordo = ''

    for(let i = 1 ; i <= flag ; i++ ){

        giros += 1

        let id = Number(question('ID: '))
        
        let peso = Number(question('Peso: '))
        
        if(peso <= magro){
            id_magro = String(id)
            magro = peso
        }else if(peso >= gordo){
            gordo = peso
            id_gordo = String(id)
        }
    }

    console.log(`......................
    Magro:${id_magro} / ${magro}
    Gordo:${id_gordo} / ${gordo}`)
}

main()