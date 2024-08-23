import {question} from 'readline-sync'

function input(text,min,max){

    const data = Number(question(text))

    if (data > min && data <= max){

        return data
    }
    else{
        input("Digite novamente: ",min,max)
    }
    return data
}

function print(text){

    console.log(text)
}