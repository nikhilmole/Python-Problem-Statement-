# Write a program which accept one number and display below pattern ?



def main():
    print("Enter number of rows :")
    n = int(input())

    for i in range(0, n, 1):
        for j in range (0, n, 1):
            print("*", end = ' ')
        print()

if __name__ == "__main__":
    main()