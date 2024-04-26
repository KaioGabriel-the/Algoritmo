import { question } from "readline-sync"

function aprovadoounao(not1,not2){
    const media = (not1 + not2)/2
    if (media >=7){
        return 'aprovado'
    }else if(media>=5 && media<7){
        return console.log(`${pf(media)}`)
        
        function pf(med){
        console.log(`................
        voce ficou de prova final
        .......................`)

        const nota_pf = get_number('digite sua nota final: ')

        const nota_final = (nota_pf + media)/2

        if(nota_final>=5){
            return 'aprovado'
        }else{
            return 'reprovado'
        }}
    }else{
        return 'reprovado'
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
    const nota1 = get_number('digite sua nota 1: ')
    const nota2 = get_number('digite sua nota 2: ')
    
    const situacao = aprovadoounao(nota1,nota2)

    console.log(`${situacao}`)

}

main()