#Write a program which contains one lamda function which accepts one parameter and return power of two
Power  = lambda iValuex: iValuex ** 2

def main():
    iValue = 0
    print("Enter Number ")
    iValue = int(input())

    iRet = Power(iValue)
    print("Power of ",iValue,"is:", iRet)

if __name__ == "__main__":
    main()