import { question } from "readline-sync"

function main(){

    const flag = Number(question('Quantidade de funcionarios: '))

    let s_salarios = 0
    let qtd_horas = 0 
    let qtd_dependencias = 0

    for(let i = 1 ; i <= flag ; i++ ){

        giros += 1

        let id = String(question('Nome: '))
        let dependencias = Number(question('Dependencias: '))
        let horas = Number(question('Quantidade de horas: '))

        let salario = (dependencias*40+ horas*12)*0.135

        s_salarios += salario
        qtd_horas += horas
        qtd_dependencias += dependencias

        console.log(`----------------
        Nome:${id}
        Salario:${salario.toFixed(2)}`)
        
    }

    console.log(`......................
    Media dos salarios:${(s_salarios/flag).toFixed(2)}
    Media das horas: ${(qtd_horas/flag).toFixed(2)}
    Media de dependencias:${(qtd_dependencias/flag).toFixed(2)}`)
}

main()