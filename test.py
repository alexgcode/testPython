"""this module is a test"""

myList=list(range(10))  #list from 0 to 9

def duplic():
    x = int(input('ingrese un numero'))
    x = x*2
    print(x)

def count_num(n):
    """metodo de contar"""
    #for x in range(0,3):

    number_string=str(n)

    print(number_string)
    nlist = list()
    for y in range(0,len(number_string)):
        nlist.append(number_string[y])

    print(nlist)
    #print(n*(x+1))

