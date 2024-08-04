def Addi(No1):
    if No1 == 0:
        return 0
    else:
        return (No1 % 10) + Addi(No1 // 10)

def main():
    print("Enter a number:")
    iValue = int(input())

    iRet = Addi(iValue)
    print("Addition of number is:", iRet)

if __name__ == "__main__":
    main()
