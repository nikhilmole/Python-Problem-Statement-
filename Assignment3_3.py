#Write a program which accept N numbers from user and store it into list.
#return minimum number from that list
def MinimumNum(No1, No2):
    iMini = No2[0]
    iNo = 0
    for iNo in range(No1):
        if(No2[iNo] < iMini):
            iMini = No2[iNo]
    print("Max number is :", iMini )

def main():
    List = []
    Size = 0
    print("How many number you want to add in list")
    Size = int(input())

    for i in range(Size):
        print('Enter a number')
        No = int(input())
        List.append(No)
    MinimumNum(Size, List)


if __name__ == "__main__":
    main()