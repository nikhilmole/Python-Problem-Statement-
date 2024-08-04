# Write a program which accept one number and display below pattern ?
#   *****
#   ****
#   ***
#   **
#   *
def main():
    print("Enter number :")
    Num = int(input())
    for i in range(0 , Num, 1):
        for j in range(0 , Num-i):
            print("*", end = "  ")
        print()



if __name__ == "__main__":
    main()