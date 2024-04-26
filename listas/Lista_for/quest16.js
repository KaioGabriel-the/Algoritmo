import {question} from 'readline-sync'

function main(){

    const numero= Number(question('Digite o limite: '))
    let n1 = 0 , n2 = 1 , newn

    for(let i = 0; i<=numero; i++){

        console.log(`${n1}`)
        newn = n1 + n2
        n1 = n2
        n2 = newn
    }

}

main()