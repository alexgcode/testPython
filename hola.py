import test

def main():
    """as Main"""
    print ('main function')
    n = int(input('ingrese un numero'))
    test.count_num(n)
    print(test.__doc__)

if __name__=='__main__':
    main()
