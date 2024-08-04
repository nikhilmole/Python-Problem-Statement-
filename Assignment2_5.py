# Write a program which accept one number from user and check whetheer number is prime or not
        
    
def main():
    
    print("Enter a number")
    Num = int(input())

    if (Num < 0):
        print("Invalid Input")
    for iNo in range(2,Num):
        if Num % iNo == 0:
            print("The number is not a prime")
            return
    else:
        print("the number is prime")

if __name__ == "__main__":
    main()
    