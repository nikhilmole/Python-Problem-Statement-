#write a  recursive program which display below pattern
i = 1
def Display(No1):
    global i 
    if (i <= No1):
        print(i, end = ' ')
        i = i + 1
        Display(No1)


def main():
    iValue = 0
    print("Enter number")
    iValue = int(input())

    Display(iValue)

if __name__ == "__main__":
    main()