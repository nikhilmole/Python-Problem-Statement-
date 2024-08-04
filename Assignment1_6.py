# Write a program which accept number from user and check whether that number is 
# positive or negative or zero ?

def Check(Value):
    if Value > 0:
        print("The number is positive..")
    elif Value < 0:
        print("The number is negative..")
    else:
        print("The number is Zero..")    


def main():
    print("Enter number :")
    No1 = int(input())
    Check(No1)

    
if __name__ == "__main__":
    main()