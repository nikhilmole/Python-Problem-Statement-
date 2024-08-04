def factorial(No1):
    if No1 == 0:
        return 1
    else:
        return No1 * factorial(No1 - 1)

def main():
    iValue = 0
    print("enter number")
    iValue = int(input())
    
    if iValue < 0:
        print("Factorial is not defined for negative numbers.")
    else:
        iRet = factorial(iValue)
        print("Factorial of", iValue, "is:", iRet)

if __name__ == "__main__":
    main()
