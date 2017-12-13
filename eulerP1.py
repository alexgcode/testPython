import numpy as np

def main():
    m=list()
    r = int(input("Enter range: "))

    for a in range(1,r):
        if a%3==0 or a%5==0:
            m.append(a)

    print("The sum of multiples of 3 or 5 is: "+str(np.sum(m)))

if __name__=="__main__":
    main()
