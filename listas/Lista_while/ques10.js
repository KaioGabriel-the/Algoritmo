import { question } from "readline-sync"

function get_positive_number(mensagem){
  // Usa Recursividade: Uma Função chamar a si mesma
  const numero = Number(question(mensagem))
  
  if (numero <= 0){
  console.log('Valor inválido!')
  return get_positive_number(mensagem)
  }
  
  return numero
}

function get_number(text){
  const numero = Number(question(text))
  return numero
 }

function calcular_garga_conteiners(lidos){
  let qtd_conteiners_lidos = 0
  let peso_total = 0
  
  while (qtd_conteiners_lidos < lidos){
  
    const peso = get_positive_number('Peso Container: ')
    peso_total = peso_total + peso
  
    qtd_conteiners_lidos += 1
  }
  
  return peso_total
}

function peso_passageiros(con_pass,con_baga){
  const peso = (con_pass * 70) + (con_baga * 10)
  return peso
}

function main(){

  const qtd_conteiners = get_positive_number('DIGITE A QUANTIDADE DE CONTENES: ')
  const ps_total = calcular_garga_conteiners(qtd_conteiners)

  let ctd_passageiros = 0
  let ctd_bagagens = 0
  let bilhete = get_number('Bilhete: ')

  while (bilhete !== 0){
    ctd_passageiros++
    const bagagens = get_number_min('Digite a contidade de Bagagens: ', 0)
    trabalho
    ctd_bagagens += bagagens
  
    bilhete = get_number('Bilhete: ')
  }

  const total_peso_fora = peso_passageiros(ctd_passageiros,ctd_bagagens) + ps_total
  const combustivel_possivel_kg = 500_000 - total_peso_fora
  const combustivel_possivel = combustivel_possivel_kg / 1.5
  const decolagem_autorizada = combustivel_possivel >= 10_000 ? 'SIM' : 'NÃO'
  
  console.log(`......PERMITIDO OU NÃO.....
  - Passageiros Embarcados: ${ctd_passageiros}
  - total de volume de bagagem: ${ctd_bagagens}
  - Peso dos Passageiros: ${peso_passageiros(ctd_passageiros,ctd_bagagens).toFixed(2)}kg
  - Peso da carga: ${ps_total.toFixed(2)}kg
  - Decolagem Autorizada? --> ${decolagem_autorizada}`)

}

main()