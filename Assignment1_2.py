#Write a program which contains one function named as chkNum Which accept  one parameter as number.
#if is even then it should display "Even number otherwise" display "Odd number on consol"

def ChkNum(No):
    if (No % 2 == 0):
        print("The number is Even")

    else:
        print("The number is Odd")

def main():
    print("Enter Any Number :")
    Ret = int(input())

    ChkNum(Ret)

#Starter
if __name__ == "__main__":
    main()