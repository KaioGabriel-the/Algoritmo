import * as utils from "./utils.js";

function main(){

    const menu = " ----- MENU ----- \n 1- INICIALIZAR VETOR; \n 2- MOSTRAR TODOS OS VALORES; \n 3- RESETAR VETOR; \n 4- VER QUANTIDADE DE ELEMENTO NA LISTA;\n 5- VER MENOR E MAIOR VALOR DA LISTA E SUAS POSIÇÕES; \n 6- SOMATÓRIO DOS VALORES; \n 7- MÉDIA DOS VALORES; \n 8- MOSTRAR TODOS OS VALORES POSITIVOS E A QUANTIDADE;\n 9- MOSTRAR TODOS OS VALORES NEGATIVOS E A QUANTIDADE; \n 10- ATUALIZAR OS VALORES ATRAVEIS DE UMA DAS REGRA;\n 11- ADICIONAR VALORES; \n 12- REMOVER ITENS POR NÚMERO EXATO; \n 13- REMOVER POR POSIÇÃO;\n 14- EDITAR ITEM POR POSIÇÃO;\n 15- SALVAR VALORES EM UM ARQUIVO; \n 0 - SAIR(SALVAMENTO AUTOMÁTICO);\n"

    utils.print(menu);

    let opction = utils.girar_menu(utils.input("Digite qual opção deseja: ",0,15))

    print("FIM DO PROGRAMA -_-")
}

main();