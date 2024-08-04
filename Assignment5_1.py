#Write a recursive program which display below pattern
i = 1
def Display(iNo):
    global i
    if(i <= iNo):
        print("*", end = ' ')
        i = i + 1
        Display(iNo)

def main():
    iValue = 0
    print("Enter Your Number")
    iValue = int(input())

    Display(iValue)
if __name__ == "__main__":
    main()