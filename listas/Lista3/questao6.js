//Leia o turno em que um aluno estuda, sendo M 
//para matutino, V para Vespertino ou N para Noturno e
//escreva a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" 
//ou "Valor Inválido!", conforme o caso.

import { question } from "readline-sync"

function saudacao(t){
    if(t=== 'matutino'){
        return 'Bom dia!'
    }else if (t=== 'vespertino'){
        return 'Boa tarde!'
    }else if(t === 'noturno'){
        return 'Boa noite!'
    }else{
        return 'erro'
    }
}

function main(){
    const turno = String(question('digite o seu turno: '))

    const mensagem = saudacao(turno)

    console.log(`${mensagem}`)
}

main()