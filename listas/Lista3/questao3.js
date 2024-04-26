//Leia uma letra e verifique se a letra digitada é vogal ou consoante.

import { question } from "readline-sync"

function verificacao(l){
    let classificao = ''
    if(l==='a'){
        return 'é vogal'
    }if(l==='e'){
        return 'é vogal'
    }if(l === 'i'){
        return 'é vogal'
    }if(l === 'o'){
        return 'é vogal'
    }if(l === 'u'){
        return 'é vogal'
    }else{
        return 'é consoante'
    }
}

function main(){
    const letra = String(question('digite uma letra: '))

    const v_c = verificacao(letra)

    console.log(`${v_c}`)
}

main()