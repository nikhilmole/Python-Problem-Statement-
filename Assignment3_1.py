#Write a program which accept N number from user and store it into list.
#Return addition of all element from that list.
#
def Add(No1, No2):
    Sum = 0
    for i in range(No1):
        Sum = Sum + No2[i]
    return Sum


def main():
    List = []
    Size = 0
    print("Enter the number of elements: ")
    Size = int(input())
    for i in range(Size):
        print("Enter the number: ")
        No = int(input())
        List.append(No)

    Ret = Add(Size, List)
    print("The addition of all list elements is:", Ret)

if __name__ == "__main__":
    main()
