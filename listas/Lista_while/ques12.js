import { question } from "readline-sync"

function get_number(text){
    const numero = Number(question(text))
    return numero
}
function main(){
    console.log('...PLACAR...')

    let pontos_a = 0
    let pontos_b = 0

    while(pontos_a <= 21 || pontos_b <= 21){
        console.log('JOGADOR A X JAGADOR B')
        let numero_de_pontos_a = get_number('PONTOS(A): ')
        pontos_a += numero_de_pontos_a

        let numero_de_pontos_b = get_number('PONTOS(B): ')
        pontos_b += numero_de_pontos_b

        if(pontos_a === 21 && pontos_b <=19){
            return console.log('JOGADOR "A" VENCEU')
        }else if(pontos_b === 21 && pontos_a <=19){
            return console.log('JOGADOR "B" VENCEU')
        }else if(pontos_a ===21 && pontos_b === 21){
            return console.log(`${EMPATE()}`)
        }
    }
    function EMPATE(){

        let pontos_a = 0
        let pontos_b = 0
        let diferença = 0
        while(pontos_a <= 21 || pontos_b <= 21){
            console.log('EMPATE ... JOGADOR A X JAGADOR B')
            let numero_de_pontos_a = get_number('PONTOS(A): ')
            pontos_a += numero_de_pontos_a
    
            let numero_de_pontos_b = get_number('PONTOS(B): ')
            pontos_b += numero_de_pontos_b

            diferença = pontos_a - pontos_b
            if(diferença === 2){
                return console.log('O JAGADOR "A" VENCEU')
            }else if(diferença === -2){
                return console.log('O JOGADOR "B" VENCEU')
            }
        }
    }
}

main()