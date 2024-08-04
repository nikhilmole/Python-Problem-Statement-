# Write a which aceept numbers from user and print that number of '*' on screen ?

def main():
    print("Enter Number :")
    No = int(input())
    i = 0
    for i in range(No):
        print("*",end = ' ')


if __name__ == "__main__":
    main()