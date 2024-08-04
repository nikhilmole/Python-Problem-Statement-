#  Write a program which contains ine function that accept one number form user and returns
# True is number is divisible by 5 otherwise return false ?
def Divisible(No):
    if (No % 5 == 0 ):
        return True
    else:
        return False

def main():
    print("Enter number :")
    Num = int(input())
    bret = False

    bret = Divisible(Num)
    if (bret == True):
        print("True....")

    else:
        print("false...")
if __name__ == "__main__":
    main()