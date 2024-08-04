#Write a program which contain filter, map, reduce in it. python application which contains one list of numbers.
#list contains the numbers which are accept from user. filter should filter out all prime numbers.Map function will  multiply each number  by 2.
#reduce will reurn  maximum number from that numbers.

from functools import reduce
def ChkPrime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1 ):
        if num % i == 0:
            return False
    else:
        return True

Multi = lambda FData : FData * 2

def Reduce (MData):
    iMax = MData[0]
    for i in range(len(MData)):
        if(MData[i] > iMax):
            iMax = MData[i]
    return iMax    


def main():
    List = []
    Size = 0
    print("Enter number of elements")
    Size = int(input())

    print("Enter numbers")
    for i in range(Size):
        No1 = int(input())
        List.append(No1)
    print("Entered elements are", List)

    FData = list(filter(ChkPrime, List))
    print("Prime numbers are :", FData)

    MData = list(map(Multi,FData))
    print("Multiplication numbers are :", MData)

    RData = Reduce(MData)
    print("Addition of all numbers are :", RData)

if __name__ == "__main__":
    main()