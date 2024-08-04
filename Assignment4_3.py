#write a pragram which contains filter, map, reduce in it. python application which
#contain one list of nmbers. lisr contain the numbers which are accepted from user.filter
#should filter out all such numbers which greater than or equal to 70 and less than or equal 
#to 90. Map function will increase each number by 10. reduce will return product of all that numbers 
from functools import reduce

Greater_Less = lambda Data1 : 70 <= Data1 <= 90

Increase = lambda FData1 : FData1 + 10

Multi = lambda A, B : A * B

def main():
    List = []
    Size = 0
    print("Enter number of elements :")
    Size = int(input())
    print("Enter your numbers")
    for i in range(Size):
        iNo = int(input())
        List.append(iNo)

    print("Your entered numbers",List)

    FData = list(filter(Greater_Less, List))
    print("Greater than 70 and Less than 90 numbers are :", FData)

    MData = list(map(Increase,FData))
    print("Numbers increase by 10 are :",MData)

    RData = reduce(Multi, MData)
    print("Data after multiplication activity " , RData)


if __name__ == "__main__":
    main()