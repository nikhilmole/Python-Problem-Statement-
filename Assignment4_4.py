#write a progrrram which contains filter,map,reduce in it. python application which contains one list of numbers.
#List contains the numbers which are accpted from user. filter should filter out all such numbers which are even.
#Map function will calculate its squarek.reduce will return addition of all that numbers
from functools import reduce
Even = lambda List1 : List1 % 2 == 0

Multi = lambda FData1 : FData1 ** 2

Add = lambda A, B : A + B

def main():
    List = []
    Size = 0

    print("Enter the number of elements : ")
    Size = int(input())
    print("Enter Numbers")
    for i in range(Size):
        iNo = int(input())
        List.append(iNo)
    print("Your entered numbers :",List)

    FData = list(filter(Even, List))
    print("Even numbers are :", FData)

    MData = list(map(Multi, FData))
    print("Multiplication of number are :",MData)

    RData = reduce(Add, MData)
    print("Addition af all numbers are", RData)


if __name__ == "__main__":
    main()