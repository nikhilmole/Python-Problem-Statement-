# Write a program which accept N numbers from user and store it into list.Accept one another
#number from user and return frequency of that number from list.
def Frequency(List1, iSize1, iFreq1):
    iCount = 0
    for i in range(iSize1):
        if List1[i] == iFreq1:
            iCount = iCount + 1
    return iCount

def main():
    List = []
    iSize = 0

    print("Enter the number of elements you want to add to the list:")
    iSize = int(input())

    for i in range(iSize):
        print("Enter a number:")
        iAdd = int(input())
        List.append(iAdd)

    print("Enter the number to find its frequency:")
    iFreq = int(input())

    iRet = Frequency(List, iSize, iFreq)
    print("Frequency is:", iRet)

if __name__ == "__main__":
    main()
