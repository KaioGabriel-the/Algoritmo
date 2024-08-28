import {question} from 'readline-sync'
import * as vetor_funcionalidaes from "./vetor_funcionalidades"
//Função responsável por criar um vetor
function creator_vector(opctin){
    //Dados automáticos
    if (opctin === 1){

    }//Vetor manual
    else if(opctin === 2){

    }//Ler um arquivo e transforma em um vetor
    else if(opctin ===3){

    }
}


export function input(text,min,max){
    const data = Number(question(text));
    const dado_filtrado = (data,min,max) => {if (min_max(data,min,max)){return data}else{input("Digite novamente: ",min,max)}};

    return dado_filtrado(data,min,max);
}

//Retorna True se o dado estiver dentro do min e o max;
function min_max(data,min,max){return data >= min && data <= max};

export function print(text){
    console.log(text);
}

//Função responsável por mostrar o menu dos vetores e retorna uma opção;
export function menu_dados(){
    const opctions = " ----- MENU(DADOS) ----- \n 1- CRIAR VETOR AUTOMÁTICO; \n 2- INFORMA DADOS AO VETOR; \n 3- CRIAR VETOR COM UM ARQUIVO;"
    print(opctions);

    return input("Digite qual opção deseja: ",1,3);
}

//função responsável por girar as opções do menu
export function girar_menu(opction){
    let vetor = []

    while (0 < opction <= 15) {
        //Carregar vetor
        if (opction === 1){
            vetor = creator_vector(menu_dados());
        }else if(opction === 2){//Mostrar todos os valores da lista na tela
            vetor_funcionalidaes.vector_show(vetor);
        }else if(opction === 3){

            
        }else if(opction === 4){

            
        }else if(opction === 5){

            
        }else if(opction === 6){

            
        }else if(opction === 7){

            
        }else if(opction === 8){

            
        }else if(opction === 9){

            
        }else if(opction === 10){

            
        }else if(opction === 11){

            
        }else if(opction === 12){

            
        }else if(opction === 13){

            
        }else if(opction === 14){

            
        }else if(opction === 15){

        }
        opction = menu_princial()
    }

}