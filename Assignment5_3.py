# Write a recursive program which display  below pattern
def Display(No1):
    
    if (No1 > 0):
        print(No1, end = ' ')
        Display(No1 - 1)


def main():
    iValue = 0
    print("Enter number")
    iValue = int(input())

    Display(iValue)

if __name__ == "__main__":
    main()