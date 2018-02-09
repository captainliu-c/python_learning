# callback_demo.py

from even import*

def getOddNum(k, getEvenNum):
    return 1 + getEvenNum(k)

def main():
    k = 1
    i = getOddNum(k, double)
    print(i)
    j = getOddNum(k, quadruple)
    print(j)

if __name__ == '__main__':
    main()
