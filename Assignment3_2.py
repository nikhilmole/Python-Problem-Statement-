#Write a program which accept N numbers from user and store it into list.Return
#mximum number rom that list.

def MaximumNum(No1, No2):
    iMax = No2[0]
    iNo = 0
    for iNo in range(No1):
        if(No2[iNo] > iMax):
            iMax = No2[iNo]
    print("Max number is :", iMax )

def main():
    List = []
    Size = 0
    print("How many number you want to add in list")
    Size = int(input())

    for i in range(Size):
        print('Enter a number')
        No = int(input())
        List.append(No)
    MaximumNum(Size, List)


if __name__ == "__main__":
    main()