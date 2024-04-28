import random

def main():

    name = str(input('Digite seu nome --> '))

    login = ''
    for i in range(0,len(name)):

      login += str(name[i])

      i+=1

    print(f'{login + '@gmail.com'}')

main()