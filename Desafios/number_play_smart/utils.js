import {question} from 'readline-sync'

export function input(text,min,max){

    const data = Number(question(text));

    const dado_filtrado = (data,min,max) => {if (min_max(data,min,max)){return data}else{input("Digite novamente: ",min,max)}};

    return dado_filtrado(data,min,max);
}

//Retorna True se o dado estiver dentro do min e o max;
function min_max(data,min,max){return data >= min && data <= max};

function print(text){
    console.log(text)};

//Finção responsável por mostrar o menu dos vetores e retorna uma opção;
export function menu_dados(){

    const opctions = " ----- MENU(DADOS) ----- \n 1- CRIAR VETOR AUTOMÁTICO; \n 2- INFORMA DADOS AO VETOR; \n 3- CRIAR VETOR COM UM ARQUIVO;"

    print(opctions);

    return input("Digite qual opção deseja: ",1,3);
}

//Função responsável por mostrar o menu principal e retorna uma opção
export function menu_princial(){

    const menu = " ----- MENU ----- \n 1- INICIALIZAR VETOR; \n 2- MOSTRAR TODOS OS VALORES; \n 3- RESETAR VETOR; \n 4- VER QUANTIDADE DE ELEMENTO NA LISTA;\n 5- VER MENOR E MAIOR VALOR DA LISTA E SUAS POSIÇÕES; \n 6- SOMATÓRIO DOS VALORES; \n 7- MÉDIA DOS VALORES; \n 8- MOSTRAR TODOS OS VALORES POSITIVOS E A QUANTIDADE;\n 9- MOSTRAR TODOS OS VALORES NEGATIVOS E A QUANTIDADE; \n 10- ATUALIZAR OS VALORES ATRAVEIS DE UMA DAS REGRA;\n 11- ADICIONAR VALORES; \n 12- REMOVER ITENS POR NÚMERO EXATO; \n 13- REMOVER POR POSIÇÃO;\n 14- EDITAR ITEM POR POSIÇÃO;\n 15- SALVAR VALORES EM UM ARQUIVO; \n 0 - SAIR(SALVAMENTO AUTOMÁTICO);\n"

    print(menu);

    return input("Digite qual opção deseja: ",0,15);
}

//função responsável por girar as opções do menu
export function girar_menu(opction){

    while ((opction,min,max) => {if (min_max(data,min,max)){return data}else{input("Digite novamente: ",min,max)}}){

        if (opction === 1){
            
        }else if(opction === 2){

            let opction = menu_princial()
        }else if(opction === 3){

            let opction = menu_princial()
        }else if(opction === 4){

            let opction = menu_princial()
        }else if(opction === 5){

            let opction = menu_princial()
        }else if(opction === 6){

            let opction = menu_princial()
        }else if(opction === 7){

            let opction = menu_princial()
        }else if(opction === 8){

            let opction = menu_princial()
        }else if(opction === 9){

            let opction = menu_princial()
        }else if(opction === 10){

            let opction = menu_princial()
        }else if(opction === 11){

            let opction = menu_princial()
        }else if(opction === 12){

            let opction = menu_princial()
        }else if(opction === 13){

            let opction = menu_princial()
        }else if(opction === 14){

            let opction = menu_princial()
        }else if(opction === 15){

            let opction = menu_princial()
        }

    }

}