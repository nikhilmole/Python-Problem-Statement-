#Write a program which contains one lambda function which accept two parameters and return its multiplication
#
Multi = lambda iNo1,iNo2 : iNo1 * iNo2
def main():
    iValue1 = 0
    iValue2 = 0
    print("Enter first number :" ,end = " ")
    iValue1 = int(input())

    print("Enter second number :" ,end = " ")
    iValue2 = int(input())

    iRet = Multi(iValue1, iValue2)
    print("Multiplication is :", iRet)


if __name__ == "__main__":
    main()