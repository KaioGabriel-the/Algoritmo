import math

def main():

    l1 = (input('')).split(' ')
    l2 = (input('')).split(' ')

    sxy = ((float(l2[0]) - float(l1[0]))**2) + \
          ((float(l2[1]) - float(l1[1]))**2)
    rxy = math.sqrt(sxy)

    print(f'{rxy:.4f}')

main()